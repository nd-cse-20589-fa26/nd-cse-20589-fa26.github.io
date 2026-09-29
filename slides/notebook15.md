---
title: "Notebook 15: Iterators, Generators"
description: "Iterators, Generators"
author: Peter Bui
keywords: notebook,sos,iterators,generators
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/notebook15.html
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

<br>

### <span class="primary">Review:</span> <span class="gold">Functional Programming</span>

<div class="font-large">

1. How do we use [map], [filter], and [lambda] to do <strong
   class="success">functional programming</strong>?

2. How do we replace [map] and [filter] with <strong class="primary">list
   comprehensions</strong>?

</div>

[map]: https://docs.python.org/3/builtins/functions.html#map
[filter]: https://docs.python.org/3/builtins/functions.html#filter
[lambda]: https://docs.python.org/3/reference/expressions.html#lambda

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

[yield]: https://docs.python.org/3/reference/simple_stmts.html#yield

---

# Generators: <span class="gold">Task Parallelism</span>

<strong class="success">Generators</strong> support problems that exhibit [task
parallelism]:

<div class="columns">

<div class="middled centered">

> <strong class="warning"> ________________________</strong> execution of the <strong
> class="success"> ________________________</strong><br>on same or different <strong
> class="caution"> _______________________</strong>.

</div>

<div class="centered">

<br>

<img src="static/img/slides16-task-parallelism.svg">

</div>

</div>

<br>

<div class="alert warning-bg centered">

In such situations, the <strong class="warning">different tasks</strong>
usually must<br>
<br>
<strong class="danger"> _________________________</strong> and
<strong class="danger"> __________________________</strong>.

</div>

[task parallelism]: https://en.wikipedia.org/wiki/Task_parallelism
