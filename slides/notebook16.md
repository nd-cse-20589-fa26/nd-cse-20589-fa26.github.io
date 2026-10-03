---
title: "Notebook 16: Concurrency and Parallelism"
description: "Concurrency and Parallelism"
author: Peter Bui
keywords: notebook,sos,concurrency,parallelism
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/notebook16.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Concurrency and Parallelism

---

# Review: <span class="gold">Iterators, Generators</span>

<div class="font-large">

1. To implement the <strong class="warning">iterator protocol</strong>, an
   **object** must implement which **methods**?

2. To implement a <strong class="success">generator</strong>, a **function**
   must use which **keyword**?

</div>

---

# Generators: <span class="gold">Trade-Offs</span>

Using the following to benchmark `odds.py` from [Reading 05]:

```bash
$ seq 10000000 | measure ./odds.py -n > /dev/null
```

[Reading 05]: reading05.html

---

# Concurrency: <span class="gold">Overview</span>

<div class="columns margin-top-0-5">

<div>

## <strong class="success">Concurrency</strong>

- <strong class="warning"> ___________________________</strong> of multiple tasks.

    <br>

- Requires <strong class="special"> _________________</strong>.

</div>

<div>

## <strong class="danger">Parallelism</strong>

- Simultaneous <strong class="caution"> ______________</strong> of
  multiple tasks.

    <br>

- Requires <strong class="info"> _________________</strong>.

</div>

</div>

<br>

<div class="alert warning-bg centered">

<strong class="success">Concurrency</strong> provides a way to <strong
class="special">structure</strong> a solution to solve a problem that may (*but
not necessarily*) be <strong class="danger">parallelizable</strong>.

</div>

---

# Concurrency: <span class="gold">Pitfalls</span>

When we have multiple tasks executing <strong
class="success">concurrently</strong>, we can encounter some <strong
class="danger">problems</strong>:

<br>

<div class="columns">

<div>

- <strong class="warning"> __________________________</strong>: multiple tasks
  compete for the <strong class="caution">same resource</strong> in an
  **unpredictable manner**.

    <br>

- <strong class="danger"> __________________________</strong>: multiple tasks
  are stuck <strong class="warning">waiting</strong> for each other.

</div>

<div class="centered">

<br>

<img src="https://upload.wikimedia.org/wikipedia/commons/2/23/Deadlock_at_a_four-way-stop.gif" class="framed">

</div>

---

# Concurrency: <span class="gold">Embarrassingly Parallel</span>

Some problems are so <strong class="caution">
__________________________________________</strong>, that is they exhibit <strong
class="warning">natural concurrency</strong>, that we label them as
[embarrassingly parallel]:

<div class="columns">

<div class="middled centered">

<img src="https://d2vfia6k6wrouk.cloudfront.net/productimages/74e8f739-cf99-4cad-bccd-b25f00affcce/images/2-pny-rtx-5090-argb-oc-epic-x-triple-fan-ra.png" width="250px">

</div>

<div class="middled centered">

<img src="https://upload.wikimedia.org/wikipedia/commons/b/ba/Hashcat-icon.png">

</div>

</div>

- Little or no <strong class="danger"> ________________________</strong> between tasks.

    <br>

- Little or no <strong class="danger"> ________________________</strong> between tasks.

[embarrassingly parallel]: https://en.wikipedia.org/wiki/Embarrassingly_parallel

---

# Concurrency: <span class="gold">Task Parallelism</span>

<strong class="success"> ______________________________</strong> support problems that
exhibit [task parallelism]:

<div class="columns">

<div class="middled">

> <strong class="warning">Concurrent</strong> execution of the <strong
> class="success">different tasks</strong> on same or different <strong
> class="caution">datasets</strong>.

</div>

<div class="centered">

<br>

<img src="static/img/slides16-task-parallelism.svg">

</div>

</div>

<br>

<div class="alert warning-bg centered">

In such situations, the <strong class="warning">different tasks</strong>
usually must <strong class="danger">communicate</strong> and <strong
class="danger">coordinate</strong> with each other.<br>The <strong
class="warning">concurrent</strong> execution of such tasks are <strong
class="special">interleaved</strong> throughout the execution of the
application.

</div>

[task parallelism]: https://en.wikipedia.org/wiki/Task_parallelism

---

# Concurrency: <span class="gold">Data Parallelism</span>

<strong class="success"> _____________________________</strong> maps well to
problems that exhibit [data parallelism]:

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

# Example: [bench.py]

Measure the **runtime** and **memory usage** of different versions of `odds.py`
from [Reading 05] multiple times:

<br>

<div class="columns-1-2">

<div>

- <strong class="success">Sequential</strong>

    <br>

- <strong class="danger">Parallel</strong>

</div>

<div>

<div class="alert warning-bg">

1. Is this [embarrassingly parallel]?

    <br>

2. Does this exhibit [data parallelism]?

    <br>

3. Does this exhibit [task parallelism]?

</div>

</div>

</div>

[Reading 05]: reading05.html
[bench.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides16/bench.py

---

# Concurrency: <span class="gold">Speedup</span>

We can compute the <strong class="success">speedup</strong> of <strong
class="danger">parallelism</strong> using the following formula:

<div class="font-large centered">

<strong class="success">Speedup</strong> = <strong
class="warning">Time<sub>sequential</sub></strong> / <strong
class="danger">Time<sub>parallel</sub></strong>

</div>

**Example**:

---

# Concurrency: <span class="gold">Amdahl's Law</span>

The <strong class="success">speedup</strong> of a program using multiple
processes is <strong class="caution">limited</strong> by

the time needed for the <strong class="warning"> _______________________</strong>
of the problem.

<div class="columns">

<div class="middled">

- If the program does not exhibit high amounts of <strong
  class="success">concurrency</strong>, then not much is gained with <strong
  class="danger">parallelism</strong>.

    <br>

- In other words, <strong class="success">speedup</strong> is limited in part
  by how much work we can <strong class="warning">divide up among different
  processes<strong class="warning">.

</div>

<div class="centered">

<br>

<img src="https://upload.wikimedia.org/wikipedia/commons/e/ea/AmdahlsLaw.svg" class="framed" width="550px">

</div>

</div>
