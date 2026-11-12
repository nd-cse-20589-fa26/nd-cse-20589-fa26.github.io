---
title: "Slides 28: Unit Tests"
description: "Unit Tests"
author: Peter Bui
keywords: lecture,sos,testing,unit tests
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides28.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Unit Tests

---

# Testing: <span class="gold">Overview</span>

When building <strong class="special">software systems</strong>, it is often necessary to
determine whether or not the program is <strong class="success">correct</strong>.  In the
absence of <strong class="danger">proofs</strong>, developers utilize
<strong class="caution">testing</strong>:

<table class="bordered">
<thead>
<th class="info-bg">Functional</th>
<th class="success-bg">Performance</th>
<th class="caution-bg">Unit</th>
</thead>
<tbody>
<tr>
<td class="centered">

Check that program performs the correct <strong class="info">functionality</strong>.

</td>
<td class="centered">

Check that program performs within the desired <strong
class="success">time</strong> and <strong class="success">resource</strong>
constraints.

</td>
<td class="centered">

Check that <strong class="caution">individual components</strong> of program
work correctly.

</td>
</tr>
</tbody>
</table>

---

# Unit Tests: [unittest]

Inspired by [JUnit], <strong class="success">Python</strong> provides
[unittest] as a <strong class="caution">unit testing</strong> framework that
provides <strong class="success">test automation</strong>.

<div class="columns">

<div class="font-smaller">

1. <strong class="caution">Test Fixtures</strong>:

    Preparation needed to perform tests, along with any cleanup.

2. <strong class="info">Test Cases</strong>:

    Group of methods that perform operations and compare outputs.

3. <strong class="danger">Test Suites</strong>:

    Collection of test cases.

4. <strong class="success">Test Runner</strong>:

    Orchestrates test execution and outputs the results.

</div>

<div>

```python
import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__:
    unittest.main()
```

</div>

</div>

[JUnit]: https://junit.org/
[unittest]: https://docs.python.org/3/library/unittest.html

---

# Unit Test: <span class="gold">Test Cases</span>

A <strong class="caution">test case</strong> is created by subclassing [unittest.TestCase]
and defining individual `test` methods:

```python
class HelloTest(unittest.TestCase):             # Test Case
    ...
    def test_01_greeting_get_default(self):     # Individual Test Method
        response = requests.get(f'http://{self.host}:{self.port}/greeting')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Hello, Unknown!')

    def test_02_greeting_get_name(self):        # Individual Test Method
        response = requests.get(f'http://{self.host}:{self.port}/greeting', params={'name': os.environ['USER']})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, f'Hello, {os.environ["USER"]}!')
    ...
```

<br>

<div class="alert info-bg centered">

The individual `test` methods are executed in **lexicographical** order.

</div>

[unittest.TestCase]: https://docs.python.org/3/library/unittest.html#unittest.TestCase

---

# Unit Test: <span class="gold">Assertions</span>

To compare responses to expected outputs, methods in <strong
class="caution">test cases</strong> can use a variety of <strong
class="danger">assertions</strong>:

<table class="bordered">
<thead>
<th class="danger-bg">Assertion</th>
<th class="info-bg">Description</th>
</thead>
<tbody>
<tr>
<td class="danger-bg"><b>assertEqual</b></td>
<td class="info-bg">Checks if arguments are equal.</td>
</tr>
<tr>
<td class="danger-bg"><b>assertTrue</b></td>
<td class="info-bg">Checks if condition is <code>True</code>.</td>
</tr>
<tr>
<td class="danger-bg"><b>assertFalse</b></td>
<td class="info-bg">Checks if condition is <code>False</code>.</td>
</tr>
<tr>
<td class="danger-bg"><b>assertRaises</b></td>
<td class="info-bg">Checks if <code>exception</code> is raised.</td>
</tr>
</tbody>
</table>

<br>

<div class="alert warning-bg centered">

If any <strong class="danger">assertions</strong> with a method fail,<br>then that individual
`test` is marked as failed.

</div>

---

# Unit Test: <span class="gold">Test Fixtures</span>

The [setUpClass] and [tearDownClass] methods are used to define instructions
that will be executed before and after **all** test methods.

```python
class HelloTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.host    = '127.0.0.1'                   # Use localhost
        cls.port    = str(find_open_port())         # Find open port
        cls.logfile = open('hello_app.log', 'w')    # Open log file
        cls.process = subprocess.Popen(             # Start web application with I/O redirection
            ['python3', '../slides27/hello_app.py', cls.host, cls.port], stdout=cls.logfile, stderr=cls.logfile
        )
        time.sleep(0.25)                            # Give time for web application to start
    @classmethod
    def tearDownClass(cls):
        cls.process.terminate()                     # Kill web application
        cls.process.wait()                          # Clean up child process
        cls.logfile.close()                         # Close log file
```

[setUpClass]: https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUpClass
[tearDownClass]: https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDownClass

---

# Unit Test: [hello_app.test]

> Write <strong class="caution">unit tests</strong> for [hello_app.py].

```bash
# Run all tests
$ ./hello_app.test
...
Ran 8 tests in 0.277s

OK

# Run individual test
$ ./hello_app.test -v HelloTest.test_01_greeting_get_default
test_01_greeting_get_default (__main__.HelloTest.test_01_greeting_get_default) ... ok
...
```

[hello_app.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides27/hello_app.py
[hello_app.test]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides28/hello_app.test
