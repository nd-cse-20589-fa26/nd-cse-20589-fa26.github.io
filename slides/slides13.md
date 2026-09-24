---
title: "Slides 13: Sorting"
description: "Sorting"
author: Peter Bui
keywords: lecture,sos,sorting
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides13.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Sorting

---

# Sorting: <span class="gold">Overview</span>

To <strong class="danger">order</strong> a <strong
class="caution">sequence</strong> of values in <strong
class="success">Python</strong>, we can use the [sorted] function on the
<strong class="caution">sequence</strong> to get a new [list]:

```python
>>> numbers = [5, 4, 7, 0, 1]   # Make a list of numbers

>>> sorted(numbers)             # Make a new list with values in ascending order
[0, 1, 4, 5, 7]

>>> number                      # Original list is unmodified
[5, 4, 7, 0, 1]
```

<br>

<div class="alert success-bg centered">

<strong class="success">Python</strong> uses [TimSort], which is a **hybrid
sorting** algorithm<br>(*ie. combines [merge sort] and [insertion sort]*) that
has an **average time complexity** of `O(nlogn)` and is considered [stable].

</div>

[sorted]: https://docs.python.org/3/builtins/functions.html#sorted
[list]: https://docs.python.org/3/builtins/stdtypes.html#typesseq-list
[merge sort]: https://en.wikipedia.org/wiki/Merge_sort
[insertion sort]: https://en.wikipedia.org/wiki/Insertion_sort
[TimSort]: https://en.wikipedia.org/wiki/Timsort
[stable]: https://en.wikipedia.org/wiki/Category:Stable_sorts

---

# Sorting: <span class="gold">In-Place</span>

Instead of create a new [list], we can <strong class="danger">order</strong> a
[list] in-place using [list.sort] method:

```python
>>> numbers = [5, 4, 7, 0, 1]   # Make a list of numbers

>>> numbers.sort()              # Sort values in ascending order in-place

>>> numbers                     # Original list is modified
[0, 1, 4, 5, 7]
```

[list.sort]: https://docs.python.org/3/builtins/stdtypes.html#list.sort

---

# Sorting: <span class="gold">Reverse</span>

By default, <strong class="success">Python</strong> orders values in
**ascending** order (*ie. from smallest to largest*).  To order in
**descending** order, set the `reverse` keyword argument in [sorted] or
[list.sort] to `True`:

```python
>>> numbers = [5, 4, 7, 0, 1]       # Make a list of numbers

>>> sorted(numbers, reverse=True)   # Make a new list with values in descending order
[7, 5, 4, 1, 0]
```

Alternatively, you can use [reversed] to generate a new sequence in the
opposite order:

```python
>>> for p in reversed(sorted(numbers)): print(p, end=' ') # Print values in descending order
7 5 4 1 0
```

[reversed]: https://docs.python.org/3/builtins/functions.html#reversed

---

# Sorting: <span class="gold">Key</span>

To change how each item in the sequence is <strong
class="warning">compared</strong> while <strong
class="danger">sorting</strong>, we can pass a <strong
class="caution">function</strong> as the `key` keyword argument to [sorted] or
[list.sort]:

```python
>>> words = 'notre dame go irish'.split()   # Make a list of words

>>> sorted(words)                           # Sort words alphabetically
['dame', 'go', 'irish', 'notre']

>>> sorted(words, key=len)                  # Sort words by length
['go', 'dame', 'notre', 'irish']
```

---

# Sorting: <span class="gold">Lambda</span>

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

---

# Sorting: <span class="gold">Multi-Factor</span>

Since <strong class="success">Python</strong> uses [TimSort], which is a
[stable] sorting algorithm, to order values by multiple factors, we can either
do:

<strong class="special">Multiple Sorts</strong> (*lowest priority to highest priority*)

```python
>>> words = 'notre dame go irish'.split()       # Make a list of words
>>> sorted(sorted(words), key=len)              # Sort alphabetically and then by length
['go', 'dame', 'irish', 'notre']
```

<strong class="gold">Complex Comparison</strong> (*highest priority to lowest priority*)

```python
>>> words = 'notre dame go irish'.split()       # Make a list of words
>>> sorted(words, key=lambda w: (len(w), w))    # Compare by length, then alphabetically
```

---

# Sorting: <span class="gold">Min, Max</span>

Sometimes, we just want to know what the **smallest** and **largest** values in
a <strong class="caution">sequence</strong> are.  For these situations, <strong
class="success">Python</strong> provides [min] and [max].

```python
>>> words = 'notre dame go irish'.split()    # Make a list of words

>>> min(words), max(words)                   # Get smallest and largest words (alphabetically)
('dame', 'notre')

>>> min(words, key=len), max(words, key=len) # Get smallest and largest words (by length)
('go', 'notre')
```

[min]: https://docs.python.org/3/builtins/functions.html#min
[max]: https://docs.python.org/3/builtins/functions.html#max
