---
title: "Slides 15: Iterators, Generators"
description: "Iterators, Generators"
author: Peter Bui
keywords: lecture,sos,iterators,generators
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides15.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Iterators, Generators

---

# Iterators, Generators: <span class="gold">Questions</span>

<div class="font-large">

1. What exactly is an <strong class="caution">iterator</strong>?

2. How do we create and use <strong class="success">generators</strong>?

</div>

---

# Perls of Wisdom

<div class="centered">

<br>
<br>

<img src="https://biwizard.wordpress.com/wp-content/uploads/2015/07/larry-wall.jpg">

<i>"We will encourage you to develop the three great virtues of a programmer:
<strong class="success">laziness</strong>, <strong
class="warning">impatience</strong>, and <strong
class="danger">hubris</strong>."  -- [Larry Wall]</i>

</div>

[Larry Wall]: https://en.wikipedia.org/wiki/Larry_Wall

---

<!-- _class: lead -->

# Iterators

---

# Iterators: <span class="gold">Iterable</span>

In <strong class="success">Python</strong>, any **object** we can loop over is
<strong class="caution">iterable</strong>:

<div class="columns">

<div>

```python
# Iterate over list
for n in [1, 2, 3, 4]:
    print(n)

# Iterate over string
for c in 'bill':
    print(c)
```

</div>

<div>

```python
# Iterate over dict
for k in os.environ:
    print(k)

# Iterate over file
for l in open('path'):
    print(l)
```

</div>

</div>

---

# Iterators: <span class="gold">Data Streams</span>

We call these **objects** <strong class="caution">iterators</strong>, since
they act like <strong class="caution">sequences</strong> except they only allow
access the <strong class="info">next item</strong> in a <strong
class="warning">stream of data</strong>:

```python
>>> i = iter(range(10))                     # Explicit iterator
>>> i
<range_iterator object at 0x7f81c3899e00>

>>> next(i)                                 # Get next item
0

>>> next(i)                                 # Get next item
1
```

---

# Iterators: <span class="gold">Like a List, But Not Quite</span>

While it is tempting to think of <strong class="caution">iterators</strong> as
[lists], they are <strong class="danger">not the same</strong>:

```python
>>> d = reversed(range(10))                 # Reverse iterator
>>> d
<range_iterator object at 0x7f81c372ebb0>

>>> next(d)                                 # Get next item
9

>>> d[0]                                    # Get first item
TypeError: 'range_iterator' object is not subscriptable
```

[lists]: https://docs.python.org/3/builtins/stdtypes.html#typesseq-list

---

# Iterators: <span class="gold">Common Iterators</span>

<strong class="success">Python</strong> provides some common <strong
class="caution">iterators</strong>:

```python
>>> x = range(10)                           # Sequence of ints
>>> r = reversed(x)                         # Reversed sequence
>>> s = sorted(r)                           # Sorted list
```

It even provides a library called [itertools] with all sorts of interesting
<strong class="caution">iterators</strong>:

``` python
>>> import itertools                        # Load library
>>> c = itertools.cycle('ABCD')             # Cyclic iterator
>>> next(c)                                 # Get first item
'A'
```

[itertools]: https://docs.python.org/3/library/itertools.html

---

# Iterators: <span class="gold">Trade-Offs</span>

Generally, looping over an <strong class="caution">iterator</strong> in <strong
class="success">Python</strong> will be both <strong
class="warning">fast</strong> and more <strong class="warning">memory
efficient</strong>.

```python
$ measure ./numbers1.py > /dev/null         # While Loop: Slow, low memory usage
7.277938 seconds        8.023438 Mbytes

$ measure ./numbers2.py > /dev/null         # For List: Fast, high memory usage
7.078453 seconds        541.996094 Mbytes

$ measure ./numbers3.py > /dev/null         # For Iterator: Fast, low memory usage
6.405172 seconds        8.011719 Mbytes
```

<br>

<div class="alert success-bg centered">

When possible, prefer to use <strong class="caution">iterators</strong>!

</div>

---

<!-- _class: lead -->

# Generators

---

# Generators: <span class="gold">Overview</span>

Rather than writing functions that return [lists], we can use the [yield]
statement to create <strong class="success">generators</strong> which behave as
<strong class="caution">iterators</strong>:

```python
def double(numbers: Iterable[int]) -> list[int]:        # List
    results = []
    for n in numbers:
        results.append(2*n)
    return results

def double(numbers: Iterable[int]) -> Iterator[int]:    # Generator
    for n in numbers:
        yield 2*n
```

[yield]: https://docs.python.org/3/reference/simple_stmts.html#yield

---

# Generators: <span class="gold">Lazy Evaluation</span>

With a <strong class="success">generator</strong>, we perform <strong
class="warning">lazy evaluation</strong>:

1. Start evaluation of <strong class="primary">function</strong> until we reach [yield]
   statement.

2. When we reach the [yield] statement, suspend or pause the <strong
   class="primary">function</strong> and return the <strong
   class="caution">expression</strong> to the caller.

3. When the <strong class="primary">function</strong> is called again, resume or continue
   where we left off.

<div class="alert success-bg centered">

A **generator** is a special class of <strong class="special">continuation</strong>.

</div>

---

# Generators: <span class="gold">Trade-Offs</span>

Using the following to benchmark `odds.py` from [Reading 05]:

```bash
$ seq 10000000 | ./measure ./odds.py -n > /dev/null
```

<table class="bordered">
<thead>
    <th>Version</th>
    <th>Runtime</th>
    <th>Memory Usage</th>
</thead>
<tbody>
<tr class="danger-bg">
    <td class="centered">Iterative</td>
    <td class="centered">7.56 s</td>
    <td class="centered">280.48 MB</td>
</tr>
<tr class="caution-bg">
    <td class="centered">Functional</td>
    <td class="centered">7.60 s</td>
    <td class="centered">&nbsp;11.80 MB</td>
</tr>
<tr class="warning-bg">
    <td class="centered">List Comprehension</td>
    <td class="centered">8.48 s</td>
    <td class="centered">278.52 MB</td>
</tr>
<tr class="success-bg">
    <td class="centered">Generator</td>
    <td class="centered">7.13 s</td>
    <td class="centered">&nbsp;11.89 MB</td>
</tr>
</tbody>
</table>

<br>

<div class="alert success-bg centered">

**Generators** are typically **fast** and use **low memory**.

</div>

[Reading 05]: reading05.html

---

# Generators: <span class="gold">Expressions</span>

To convert a [list comprehension] to a [generator expression], we simply
replace the `[]` with `()`:

```python
# List Comprehension
>>> [n*2 for n in range(5)]
[0, 2, 4, 6, 8]

# Generator Expression
>>> (n*2 for n in range(5))
<generator object <genexpr> at 0x7f27b005d080>
```

[list comprehension]: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
[generator expression]: https://docs.python.org/3/reference/expressions.html#generator-expressions

---

# Generators: <span class="gold">Task Parallelism</span>

<strong class="success">Generators</strong> support problems that exhibit [task
parallelism]:

> <strong class="warning">Concurrent</strong> execution of the <strong
> class="success">different tasks</strong> on same or different <strong
> class="caution">datasets</strong>.

<br>

<div class="alert warning-bg centered">

In such situations, the <strong class="warning">different tasks</strong>
usually must <strong class="danger">communicate</strong> and <strong
class="danger">coordinate</strong> with each other.  The <strong
class="warning">concurrent</strong> execution of such tasks are <strong
class="special">interleaved</strong> throughout the execution of the
application.

</div>

[task parallelism]: https://en.wikipedia.org/wiki/Task_parallelism
