---
title: "Notebook 17: Object-Oriented Programming"
description: "Object-Oriented Programming"
author: Peter Bui
keywords: notebook,sos,object-oriented programming
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/notebook17.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Object-Oriented Programming

---

# OOP: <span class="gold">Questions</span>

<div class="font-large">

1. What are the **four** core <strong class="info">principles</strong> of
   <strong class="primary">object-oriented programming</strong>?

2. How do we define our own <strong class="caution">class</strong> in
   <strong class="success">Python</strong>?

3. What are <strong class="special">dunder/magic methods</strong>?

</div>

---

# OOP: <span class="gold">Overview</span>

<div class="columns">

<div>

[Object-oriented programming] is a <strong class="special">programming
paradigm</strong> that organizes software design

around <strong class="danger"> ________________________</strong>

called <strong class="primary"> ________________________</strong>

(ie. <strong class="info"> _________________________</strong>)

and the <strong class="warning"> _______________________</strong>

that operate on such objects

(ie. <strong class="success"> ________________________</strong>).

</div>

<div class="alert caution-bg">

Everything in <strong class="success">Python</strong> is an <strong
class="primary">object</strong>:

- Has a <strong class="caution"> __________________</strong>

    <br>

- Has <strong class="info">      ____________________</strong>

    <br>

- Has <strong class="warning">   ____________________</strong>

</div>

</div>

[Object-oriented programming]: https://en.wikipedia.org/wiki/Object-oriented_programming

---

# OOP: <span class="gold">Principles</span>

<table class="bordered">
<tbody>
<tr>
<td class="caution-bg centered" width="500px">

<strong> ______________________________</strong>

*Hide implementation* details and exposing only the essential functionality.

<br>

</td>
<td class="success-bg centered" width="500px">

<strong> ______________________________</strong>

**Treat objects** as instances of the **same base type**, as long as they
implement a **common interface**.

</td>
</tr>
<tr>
<td class="special-bg centered" width="500px">

<strong> ______________________________</strong>

**Bundle data** (*attributes*) and **behaviors** (*methods*) to create a
cohesive unit.

</td>
<td class="warning-bg centered" width="500px">

<strong> ______________________________</strong>

Enable creation **hierarchical relationships** between units to allow for
**code reuse**.

</td>
</tr>
</tbody>
</table>

---

# OOP: <span class="gold">Class</span>

<div class="columns">

<div>

To model <strong class="danger">data</strong>, we define a <strong
class="caution">class</strong> to serve as a

<strong class="info"> _____________________________</strong>
for new <strong class="primary">objects</strong> of that type.  Each <strong
class="caution">class</strong> consists of:

<div class="font-smaller">

1. <strong class="info">    _____________________________</strong>:

    <strong class="success">Variables</strong> that store internal <strong
    class="danger">data</strong>.

    <br>

2. <strong class="warning"> _____________________________</strong>:

    <strong class="success">Functions</strong> that define the behavior and
    operations of the <strong class="primary">object</strong>.

</div>

</div>

<div>

<div class="alert warning-bg">

**[ ] Constructor**

**[ ] Attributes**

**[ ] Methods**

**[ ] Decorators**

**[ ] Dunder/Magic Methods**

**[ ] Dataclass**

</div>

</div>

</div>

---

# OOP: <span class="gold">Context Manager Protocol</span>

In <strong class="success">Python</strong>, the `with` statement uses the
<strong class="warning">context manager protocol</strong>, which requires that
the <strong class="primary">object</strong> implements the `__enter__` and
`__exit__` methods. (**example**: [timer.py])

<div class="columns">

<div>

```python
@dataclass
class Timer:

    ...

    # Context Manager Protocol

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
```

</div>

<div>

```python
# Use timer as context manager

with Timer() as timer:  # Calls timer.__enter__()
    for _ in range(5):
        print(f'Loop: {timer.elapsed_time:0.2f}')
        time.sleep(1)

# Calls timer.__exit__()

time.sleep(5)

print(f'Final: {timer.elapsed_time:0.2f}')
```

</div>

</div>

[timer.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides17/timer.py
