---
title: "Slides 17: Object-Oriented Programming"
description: "Object-Oriente Programming"
author: Peter Bui
keywords: lecture,sos,object-oriented programming
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides17.html
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
paradigm</strong> that organizes software design around <strong
class="danger">data</strong> called <strong class="primary">objects</strong>
(ie. <strong class="info">structures</strong>) and the <strong
class="warning">methods</strong> that operate on such objects (ie.  <strong
class="success">functions</strong>).

</div>

<div class="alert caution-bg">

Everything in <strong class="success">Python</strong> is an <strong
class="primary">object</strong>:

- Has a <strong class="caution">type</strong>

- Has <strong class="info">attributes</strong> (<strong
  class="danger">data</strong>)

- Has <strong class="warning">methods</strong> (<strong
  class="success">functions</strong>)

</div>

</div>

```python
>>> s = 'hello, world'          # Create string object
>>> dir(s)                      # View attributes and methods of string object
['__add__', '__class__', ... ]
>>> s.upper()                   # Call upper method of string object
'HELLO, WORLD'
```

[Object-oriented programming]: https://en.wikipedia.org/wiki/Object-oriented_programming

---

# OOP: <span class="gold">Principles</span>

<table class="bordered">
<tbody>
<tr>
<td class="caution-bg centered" width="500px">
<strong>Data Abstraction</strong>

**Hide implementation** details and exposing only the essential functionality.

<br>

</td>
<td class="success-bg centered" width="500px">
<strong>Polymorphism</strong>

**Treat objects** as instances of the **same base type**, as long as they
implement a **common interface**.

</td>
</tr>
<tr>
<td class="special-bg centered" width="500px">
<strong>Encapsulation</strong>

**Bundle data** (*attributes*) and **behaviors** (*methods*) to create a
cohesive unit.

<br>

</td>
<td class="warning-bg centered" width="500px">
<strong>Inheritance</strong>

Enable creation **hierarchical relationships** between units to allow for
**code reuse**.

</td>
</tr>
</tbody>
</table>

---

# OOP: <span class="gold">Class</span>

<div class="columns-2-3">

<div>

To model <strong class="danger">data</strong>, we define a <strong
class="caution">class</strong> to serve as a <strong
class="info">template</strong> for new <strong class="primary">objects</strong>
of that type.  Each <strong class="caution">class</strong> consists of:

<div class="font-smaller">

1. <strong class="info">Attributes</strong>:

    <strong class="success">Variables</strong> that store internal <strong
    class="danger">data</strong>.

2. <strong class="warning">Methods</strong>:

    <strong class="success">Functions</strong> that define the behavior and
    operations of the <strong class="primary">object</strong>.

</div>

</div>

<div>

```python
class Timer:
    # Constructor
    def __init__(self, start_time: Optional[float]=None):
        self.start_time = start_time or time.time()
        self.stop_time  = 0.0

    # Methods
    def stop(self):
        self.stop_time  = time.time()

    def reset(self):
        self.start_time = time.time()

    @property
    def elapsed_time(self) -> float:
        stop_time = self.stop_time or time.time()
        return stop_time - self.start_time

    # Dunder/Magic Method (str)
    def __str__(self) -> str:
        return f'Timer({self.start_time}, {self.stop_time})'
```

</div>

</div>

---

# OOP: <span class="gold">Constructor, Methods, Attributes</span>

<div class="columns-2-3">

<div>

<div class="alert">

Each <strong class="caution">class</strong> is a series of <strong
class="warning">method</strong> definitions.

</div>

<div class="alert info-bg font-small centered">

The <strong class="warning"> __init__ method</strong> is the <strong
class="special">constructor</strong> of the <strong
class="caution">class</strong> is called whenever we call the <strong
class="caution">class</strong> name as if it were a <strong
class="success">function</strong>.

</div>

<br>

<div class="alert success-bg font-small centered">

The first argument to each <strong class="warning">method</strong> is <strong
class="success">self</strong>, which represents the <strong
class="primary">current instance</strong>.

</div>

<br>

<div class="alert danger-bg font-small centered">

Internal <strong class="info">attributes</strong> of each <strong
class="primary">object</strong> can be accessed using the **.** notation:
**object.attribute**.

</div>

</div>

<div>

```python
class Timer:
    # Constructor
    def __init__(self, start_time: Optional[float]=None):
        self.start_time = start_time or time.time()
        self.stop_time  = 0.0

    # Methods
    def stop(self):
        self.stop_time  = time.time()

    def reset(self):
        self.start_time = time.time()

    @property
    def elapsed_time(self) -> float:
        stop_time = self.stop_time or time.time()
        return stop_time - self.start_time

    # Dunder/Magic Method (str)
    def __str__(self) -> str:
        return f'Timer({self.start_time}, {self.stop_time})'
```

</div>

</div>

---

# OOP: <span class="gold">Dunder/Magic Methods</span>

<div class="columns-2-3">

<div>

<div class="alert">

In <strong class="success">Python</strong>, certain <strong
class="special">dunder</strong> or <strong class="special">magic
method</strong> names correspond to different <strong class="info">built-in
operations</strong> or <strong class="info">functions</strong>.

</div>

<div class="alert special-bg font-small">

For example, whenever <strong class="info">str()</strong> is called on an
<strong class="primary">object</strong>, <strong
class="success">Python</strong> calls the <strong
class="special">__str__</strong> method of that <strong
class="primary">object</strong> to get a <strong
class="success">string</strong> representation of the <strong
class="primary">object</strong>.

</div>

</div>

<div>

```python
class Timer:
    # Constructor
    def __init__(self, start_time: Optional[float]=None):
        self.start_time = start_time or time.time()
        self.stop_time  = 0.0

    # Methods
    def stop(self):
        self.stop_time  = time.time()

    def reset(self):
        self.start_time = time.time()

    def elapsed_time(self) -> float:
        stop_time = self.stop_time or time.time()
        return stop_time - self.start_time

    # Dunder/Magic Method (str)
    def __str__(self) -> str:
        return f'Timer({self.start_time}, {self.stop_time})'
```

</div>

</div>

---

# OOP: <span class="gold">Data Class, Decorators</span>

<div class="columns-2-3">

<div>

<div class="alert">

We can declare a [dataclass], which is like a `struct` in <strong
class="danger">C</strong>.

</div>

<div class="alert warning-bg font-small">

Functions with <strong class="comment">@</strong> are called <strong
class="comment">decorators</strong>.  They modify the code (<strong
class="caution">classes</strong> or <strong class="success">functions</strong>)
that come after them.

</div>

<br>

<div class="alert caution-bg font-small">

<strong class="comment">@dataclass</strong> provides the <strong
class="caution">class</strong> with automatic <strong
class="special">constructor</strong> and <strong
class="special">__str__</strong> <strong class="warning">methods</strong>.

<strong class="comment">@property</strong> provides the <strong
class="caution">class</strong> with a **dynamic** <strong
class="info">attribute</strong> that executes the corresponding <strong
class="warning">method</strong> when accessed.

</div>

</div>

<div>

```python
@dataclass
class Timer:
    # Attributes
    start_time: float = time.time()
    stop_time:  float = 0.0

    # Methods
    def stop(self):
        self.stop_time  = time.time()

    def reset(self):
        self.start_time = time.time()

    @property
    def elapsed_time(self) -> float:
        stop_time = self.stop_time or time.time()
        return stop_time - self.start_time
```

</div>

</div>

[dataclass]: https://docs.python.org/3/library/dataclasses.html

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
