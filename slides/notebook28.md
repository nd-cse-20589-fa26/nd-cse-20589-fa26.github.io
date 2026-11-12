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

# REST: <span class="gold">Review</span>

<strong class="special">REST</strong> (<i><b>re</b>presentational **s**tate
**t**ransfer</i>) and is a <strong class="success">software architecture
style</strong> that defines a <strong class="strong">pattern</strong> for
<strong class="info">client</strong> and <strong class="danger">server</strong>
interactions.

<div class="centered">

<img src="static/img/software-systems.svg">

</div>

---

# REST: <span class="gold">Endpoints</span>

To define a <strong class="special">REST</strong> API, it is necessary to
describe the [HTTP] methods and <strong class="success">endpoints</strong> (ie.
<strong class="success">URL paths</strong>), along with any <strong
class="danger">parameters</strong> they may take.

<br>

<table class="bordered font-smaller">
<thead>
    <th class="special-bg">HTTP Method</th>
    <th class="special-bg">API Endpoint</th>
    <th class="special-bg">Description</th>
    <th class="special-bg">Query Data</th>
    <th class="special-bg">Form Data</th>
</thead>
<tbody>
<tr class="info-bg">
    <td class="centered"><b>GET</b></td>
    <td>/greeting</td>
    <td>Get greeting for <code>name</code></td>
    <td><code>name<code>: <code>str</code></td>
    <td></td>
</tr>
<tr class="success-bg">
    <td class="centered"><b>POST</b>/<b>PUT</b></td>
    <td>/greeting</td>
    <td>Set greeting to <code>greeting<code></td>
    <td></td>
    <td><code>greeting<code>: <code>str</code></td>
</tr>
</tbody>
</table>

[HTTP]: https://en.wikipedia.org/wiki/HTTP

---

# Testing: <span class="gold">Overview</span>

When building <strong class="special">software systems</strong>, it is often necessary to
determine whether or not the program is <strong class="success">correct</strong>.  In the
absence of <strong class="danger">proofs</strong>, developers utilize
<strong class="caution">testing</strong>:

<br>

<table class="bordered">
<thead>
<th class="info-bg">Functional</th>
<th class="success-bg">Performance</th>
<th class="caution-bg">Unit</th>
</thead>
<tbody>
<tr>
<td class="centered info-bg" width="350px">

<br>
<br>
<br>
<br>
<br>

</td>
<td class="centered success-bg" width="350px">

<br>
<br>
<br>
<br>
<br>

</td>
<td class="centered caution-bg" width="350px">

<br>
<br>
<br>
<br>
<br>

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

<br>

1. <strong class="caution"> ______________________________</strong>:

    <br>

2. <strong class="info">    ______________________________</strong>:

    <br>

3. <strong class="danger">  ______________________________</strong>:

    <br>

4. <strong class="success"> ______________________________</strong>:


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
