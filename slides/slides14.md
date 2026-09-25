---
title: "Slides 14: Functional Programming"
description: "Functional Programming"
author: Peter Bui
keywords: lecture,sos,functional programming
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides14.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Functional Programming

---

# Functional Programming: <span class="gold">Questions</span>

<div class="font-large">

1. What is <strong class="success">functional programming</strong> and how is
   it different from <strong class="danger">imperative programming</strong>?

2. Why are [map], [filter], and [reduce] called <strong
   class="special">higher-order functions</strong>?

3. How do we replace [map] and [filter] with <strong class="primary">list
   comprehensions</strong>?

</div>

[map]: https://docs.python.org/3/builtins/functions.html#map
[filter]: https://docs.python.org/3/builtins/functions.html#filter
[reduce]: https://docs.python.org/3/library/functools.html#functools.reduce

---

# Functional Programming: <span class="gold">Paradigm</span>

<div class="columns margin-top-0-5">

<div>

## <strong class="danger">Imperative</strong>

An <strong class="danger">imperative program</strong> is written as a sequence
of <strong class="caution">instructions</strong>, telling the computer,
what to do step-by-step.

```python
doubles = []
for n in numbers:
    doubles.append(n * 2)
```

</div>

<div>

## <strong class="success">Functional</strong>

A <strong class="success">functional program</strong> is a <strong
class="warning">composition</strong> of <strong
class="primary">functions</strong>.

```python
doubles = map(lambda n: 2*n, numbers)
```

<br>

<div class="alert caution-bg centered font-smaller">

<i>"<strong class="success">Functional programming</strong> is like describing
your problem to a <strong class="success">mathematician</strong>.  <strong
class="danger">Imperative programming</strong> is like giving instructions to
an <strong class="danger">idiot</strong>."</i>

</div>

</div>

</div>

---

# Functional Programming: <span class="gold">Overview</span>

<strong class="success">Functional programming</strong> is a <strong
class="primary">programming paradigm</strong> that emphasizes the <strong
class="warning">composition</strong> of <strong
class="primary">functions</strong> to solve problems:

- <strong class="primary">Functions</strong> always return <strong
  class="caution">same output</strong> for given input.

- <strong class="caution">Stateless</strong> (<i class="muted">no
  side-effects</i>).

- Order of evaluation <strong class="caution">undefined</strong>.

- Emphasizes <strong class="caution">divide</strong> and <strong
  class="caution">conquer</strong>.

---

# Functional Programming: <span class="gold">Map</span>

To transform a <strong class="caution">sequence</strong> into another <strong
class="caution">sequence</strong>, we can use the [map] <strong
class="primary">higher order function</strong>:

<div class="columns">

<div>

```python
map(func, seq)
```

<br>

<div class="alert info-bg centered">

[map] takes a <strong class="primary">function</strong> `func` <strong
class="success">applies</strong> it to each of the elements in the <strong
class="caution">sequence</strong> `seq`.

</div>

<br>

<div class="alert warning-bg centered">

**Note**: [map] returns a [generator], not a [list].

</div>

</div>

<div>

```python
# Convert all strings into a
# list of floats
>>> strings = ['3.14', '2.71', '1.0']
>>> list(map(float, strings))
[3.14, 2.71, 1.0]
```

<div class="centered">

<i>In this example, the <strong class="primary">function</strong> `float` is
applied to each string in `strings` and the result is converted into a new
[list].</i>

</div>

</div>

</div>

[list]: https://docs.python.org/3/builtins/stdtypes.html#typesseq-list
[generator]: https://docs.python.org/3/glossary.html#term-generator
[generators]: https://docs.python.org/3/glossary.html#term-generator

---

# Functional Programming: <span class="gold">Operator</span>

The <strong class="caution">operator</strong> module that includes useful
<strong class="primary">functions</strong> for common operations that we can
utilize in our programs.

```python
# Load the add function from the operator module
>>> from operator import add

# Declare two lists of numbers
>>> A = [0, 1, 2, 3, 4]
>>> B = [4, 3, 2, 1, 0]

# Apply add function to both A and B (pair-wise)
>>> map(add, A, B)
[4, 4, 4, 4, 4]
```

---

# Functional Programming: <span class="gold">Lambda</span>

To quickly define short <strong class="primary">functions</strong>, we can use
the [lambda] expression which allows us to create one-line <strong
class="primary">functions</strong> that consist of a single <strong
class="caution">expression</strong>.

```python
# Declare two lists of numbers
>>> A = [0, 1, 2, 3, 4]
>>> B = [4, 3, 2, 1, 0]

# Apply add function to both A and B (pair-wise)
>>> map(lambda a, b: a + b, A, B)
[4, 4, 4, 4, 4]
```

[lambda]: https://docs.python.org/3/reference/expressions.html#lambda
[lambdas]: https://docs.python.org/3/reference/expressions.html#lambda

---

# Functional Programming: <span class="gold">Reduce</span>

To aggregate or collect items from a <strong class="caution">sequence</strong>
into a <strong class="warning">single</strong> value, <strong
class="success">Python</strong> provides the [reduce] function.

```python
>>> from functools import reduce # Load the reduce function from the functools module

>>> numbers = [4, 5, 4, 0, 6]                       # Declare lists of number

>>> reduce(add, numbers, 0)                         # Sum of sequence of numbers
19

>>> reduce(lambda a, b: a if a < b else b, numbers) # Min of sequence of numbers
0

>>> reduce(lambda a, b: a if a > b else b, numbers) # Max of sequence of numbers
6
```

---

# Functional Programming: <span class="gold">Filter</span>

To traverse a <strong class="caution">sequence</strong> of values and <strong
class="warning">extract</strong> a few particular values, <strong
class="success">Python</strong> provides the [filter] function:

<div class="columns">

<div>

```python
filter(func, seq)
```

<br>

<div class="alert info-bg centered">

[filter] takes a <strong class="primary">function</strong> `func` <strong
class="success">applies</strong> it to each of the elements in the <strong
class="caution">sequence</strong> `seq`.  If the result is `True`, then the
element is included in the resulting <strong class="caution">sequence</strong>.

</div>

<br>

</div>

<div>

```python
# Declare a list of numbers
>>> numbers = [9, 2, 8, 6, 7]

# Extract only even numbers
>>> list(filter(lambda x: not x % 2, numbers))
[2, 8, 6]
```

<br>

<div class="alert warning-bg centered">

**Note**: [filter] returns a [generator], not a [list].

</div>

</div>

</div>

---

# List Comprehensions: <span class="gold">Overview</span>

Because [map] and [filter] is so common and [lambdas] can be a bit tricky to
use, <strong class="success">Python</strong> provides some <strong
class="special">syntactic sugar</strong> called [list comprehensions] which
allow us to concisely construct new [lists].

```python
# List Comprehension Structure
list_comprehension = [
    element            # Return value for each element in sequence
    for element in seq # Sequence to loop over
    if condition       # Condition used to filter elements (optional)
]
```

[list comprehensions]: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
[lists]: https://docs.python.org/3/builtins/stdtypes.html#typesseq-list

---

# List Comprehensions: <span class="gold">Map</span>

To <strong class="info">double</strong> the elements in a [list], we can use [map]:

```python
# Using map
>>> list(map(lambda x: 2*x, [0, 1, 2, 3, 4]))
[0, 2, 4, 6, 8]
```

Alternatively, we could do the following with [list comprehensions]:

```python
# Using list comprehension
>>> [2*x for x in [0, 1, 2, 3, 4]]
[0, 2, 4, 6, 8]
```

---

# List Comprehensions: <span class="gold">Filter</span>

To [filter] a [list] for even numbers:

```python
# Using filter
>>> list(filter(lambda x: not x % 2, [0, 1, 2, 3, 4]))
[0, 2, 4]
```

With [list comprehensions]:

```python
# Using list comprehension
>>> [x for x in [0, 1, 2, 3, 4] if not x % 2]
[0, 2, 4]
```

---

# List Comprehensions: <span class="gold">Map + Filter</span>

To both <strong class="warning">extract</strong> even numbers and
<strong class="info">double</strong> them:

```python
# Using map and filter
>>> list(map(lambda x: 2*x, filter(lambda x: not x % 2, [0, 1, 2, 3, 4])))
[0, 4, 8]
```

With [list comprehensions]:

```python
# Using list comprehension
>>> [2*x for x in [0, 1, 2, 3, 4] if not x % 2]
[0, 4, 8]
```

---

# FP: <span class="gold">vs List Comprehension</span>

You can usually use either [map] and [filter] or [list comprehensions] (*or
both together!*).  However, you should remember the following:

1. [map] and [filter] return [generators], not [lists].

2. [list comprehensions] always return [lists].

<div class="alert warning-bg centered">

This can have a <strong class="danger">significant impact</strong> on your<br>
<strong class="warning">memory usage</strong> and <strong
class="success">performance</strong>.

</div>

---

# FP: <span class="gold">Implicit Concurrency</span>

If we modify our programs to use a <strong class="success">functional
programming</strong> approach via [map], we get <strong
class="success">concurrency</strong> as a <strong
class="danger">side-effect</strong> for free:

<div class="columns">

<div>

```python
# Instead of this
for item in stream:
    compute(item)
```

<br>

<div class="alert danger-bg centered">

<i>Inherently **sequential**</i>

</div>

</div>

<div>

```python
# Do this
map(compute, stream)
```

<br>
<br>

<div class="alert success-bg centered">

<i>Possibly **concurrent**</i>

</div>

</div>

</div>

---

# FP: <span class="gold">Concurrency and Parallelism</span>

<div class="columns margin-top-0-5">

<div>

## <strong class="success">Concurrency</strong>

- <strong class="warning">Composition</strong> of independently execution
  computations.

- Concerned about <strong class="special">structure</strong>.

</div>

<div>

## <strong class="danger">Parallelism</strong>

- <strong class="caution">Simultaneous</strong> execution of (*possibly related*)
  computations.

- Concerned with <strong class="info">execution</strong>.

</div>

<br>

</div>

<div class="alert warning-bg centered">

<strong class="success">Concurrency</strong> provides a way to <strong
class="special">structure</strong> a solution to solve a problem that may (*but
not necessarily*) be <strong class="danger">parallelizable</strong>.

</div>

---

# FP: <span class="gold">Data Parallelism</span>

<strong class="success">Functional programming</strong> maps well to problems that exhibit
[data parallelism]:

<div class="columns">

<div class="middled">

> <strong class="warning">Concurrent</strong> execution of the <strong
> class="success">same task</strong> across the elements of a <strong
> class="caution">dataset</strong>.

</div>

<div class="centered">

<img src="static/img/slides16-data-parallelism.svg">

</div>

</div>

<br>

<div class="alert warning-bg centered">

In such situations, the <strong class="caution">dataset</strong> normally
exhibits [data independence], meaning each element can be processed <strong
class="special">independently</strong> of the other.

</div>

[data parallelism]: https://en.wikipedia.org/wiki/Data_parallelism
[data independence]: https://en.wikipedia.org/wiki/Data_independence

---

# FP: <span class="gold">Concurrent Futures</span>

Once our program is structured to use [map], we can use the
[concurrent.futures] module to perform <strong class="danger">parallel</strong> execution:

```python
# Load concurrent.futures module
import concurrent.futures

# Create a pool of 4 processes
with concurrent.futures.ProcessPoolExecutor(4) as executor:
    # Execute compute on stream in parallel
    executor.map(compute, stream)
```

[concurrent.futures]: https://docs.python.org/3/library/concurrent.futures.html
