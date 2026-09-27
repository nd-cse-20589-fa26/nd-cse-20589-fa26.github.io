---
title: "Notebook 14: Functional Programming"
description: "Functional Programming"
author: Peter Bui
keywords: notebook,sos,functional programming
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/notebook14.html
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

# Review: <span class="gold">Sorting, Lambda</span>

Rather than defining a <strong class="caution">function</strong> separately, we
can use a [lambda] expression to make an **anonymous** <strong
class="caution">function</strong> inline:

```python
>>> words = 'notre dame go irish'.split()   # Make a list of words

>>> def last(w): return w[-1]               # Function that returns last letter

>>> sorted(words, key=last)                 # Sort words by last letter using function
['notre', 'dame', 'irish', 'go']

>>> sorted(words, key=lambda w: w[-1])      # Sort words by last letter using lambda
['notre', 'dame', 'irish', 'go']
```

[lambda]: https://docs.python.org/3/reference/expressions.html#lambda
[lambdas]: https://docs.python.org/3/reference/expressions.html#lambda

---

# Functional Programming: <span class="gold">Map</span>

To transform a <strong class="caution">sequence</strong> into another <strong
class="caution">sequence</strong>, we can use the [map] <strong
class="primary">higher order function</strong>:

```python
# Conceptual implementation of map
def map(func: Callable, seq: Iterable) -> Iterator:
    for item in seq:
        yield func(item)
```

<br>

<div class="alert info-bg centered">

[map] takes a <strong class="primary">function</strong> `func` <strong
class="success">applies</strong> it to each of the elements in the <strong
class="caution">sequence</strong> `seq` and returns the results of that
application.

</div>

[list]: https://docs.python.org/3/builtins/stdtypes.html#typesseq-list
[generator]: https://docs.python.org/3/glossary.html#term-generator
[generators]: https://docs.python.org/3/glossary.html#term-generator

---

# Functional Programming: <span class="gold">Filter</span>

To traverse a <strong class="caution">sequence</strong> of values and <strong
class="warning">extract</strong> a few particular values, <strong
class="success">Python</strong> provides the [filter] function:

```python
# Conceptual implementation of filter
def filter(func: Callable, seq: Iterable) -> Iterator:
    for item in seq:
        if func(item):
            yield item
```

<br>

<div class="alert info-bg centered">

[filter] takes a <strong class="primary">function</strong> `func` <strong
class="success">applies</strong> it to each of the elements in the <strong
class="caution">sequence</strong> `seq`.  If the result is `True`, then the
element is included in the resulting <strong class="caution">sequence</strong>.

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
    item            # Return value for each item in sequence
    for item in seq # Sequence to loop over
    if condition    # Condition used to filter items (optional)
]
```

[list comprehensions]: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
[lists]: https://docs.python.org/3/builtins/stdtypes.html#typesseq-list

---

# FP: <span class="gold">Paradigms</span>

<table class="bordered">
<thead>
<th class="danger-bg">Imperative</th>
<th class="success-bg">Functional</th>
</thead>
<tbody>
<tr>
    <td class="danger-bg" width="600px">Programs as a <strong class="danger">sequence</strong> of instructions</td>
    <td class="success-bg" width="600px"><br><br><br></td>
</tr>
<tr>
    <td class="danger-bg" width="600px"><strong class="danger">Change state</strong> and <strong class="danger">mutate</strong> data (<i>variables<i>)</td>
    <td class="success-bg" width="600px"><br><br><br></td>
</tr>
<tr>
    <td class="danger-bg" width="600px"><strong class="danger">Explicitly enumerate order</strong> of operations</td>
    <td class="success-bg" width="600px"><br><br><br></td>
</tr>
</tbody>
</table>


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

<br>
<br>
<br>

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

<br>
<br>
<br>

</div>

</div>

</div>

---

# FP: <span class="gold">Data Parallelism</span>

<strong class="success">Functional programming</strong> maps well to problems
that exhibit [data parallelism]:

<div class="columns centered">

<div class="middled">

> <strong class="warning"> ________________________</strong> execution of the <strong
> class="success"> ________________________</strong> across the elements of a <strong
> class="caution"> _______________________</strong>.

</div>

<div class="centered">

<img src="static/img/slides16-data-parallelism.svg">

</div>

</div>

<br>

<div class="alert warning-bg centered">

In such situations, the <strong class="caution">dataset</strong> normally
exhibits<br><br><strong> ________________________________________</strong>.

</div>

[data parallelism]: https://en.wikipedia.org/wiki/Data_parallelism
[data independence]: https://en.wikipedia.org/wiki/Data_independence

---

# FP: <span class="gold">Concurrent Futures</span>

Once our program is structured to use [map], we can use the
[concurrent.futures] module to perform <strong class="danger">parallel</strong>
execution:

```python
# Load concurrent.futures module
import concurrent.futures

# Create a pool of 4 processes
with concurrent.futures.ProcessPoolExecutor(4) as executor:
    # Execute compute on stream in parallel
    executor.map(compute, stream)
```

[concurrent.futures]: https://docs.python.org/3/library/concurrent.futures.html
