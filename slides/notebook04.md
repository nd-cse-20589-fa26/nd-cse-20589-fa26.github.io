---
title: "Notebook 04: Python, Control Flow, Modules"
description: "Python, Control Flow, Modules"
author: Peter Bui
keywords: notebook,sos,python,control flow,modules
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/notebook04.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Python, Control Flow, Modules

---

<!-- _class: lead -->

# Python

---

# Python: <strong class="gold">Overview</strong>

Python is an <strong class="caution">interpreted</strong>, <strong
class="warning">object-oriented</strong>, <strong
class="success">high-level</strong> **programming language** with dynamic
semantics.

<div class="columns">

<div class="font-smaller">

- Encourages very <strong class="info">readable</strong> and <strong
  class="info">well structured</strong> code.

- Rich <strong class="caution">ecosystem of libraries</strong> and <strong
  class="caution">frameworks</strong> ([NumPy], [Pandas], [Django], [Flask],
  [TensorFlow], [PyTorch], etc.).

- <strong class="success">Free</strong> and <strong class="success">open
  source</strong>, widely spread, with vibrant <strong
  class="special">community</strong>.

[NumPy]: https://numpy.org/
[Pandas]: https://pandas.pydata.org/
[Django]: https://www.djangoproject.com/
[Flask]: https://flask.palletsprojects.com/en/stable/
[TensorFlow]: https://www.tensorflow.org/
[PyTorch]: https://pytorch.org/

</div>

<div class="centered middled">

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/500px-Python_logo_and_wordmark.svg.png">

</div>

</div>

---

# Python: <strong class="gold">Industry Adoption</strong>

<br>

<div class="slide-centered">

<img src="static/img/slides04-python-industry-adoption.png" height="550px">

</div>

---

# Python: <strong class="gold">Antigravity</strong>

<br>

<div class="slide-centered">

<a href="https://xkcd.com/353/">
<img src="https://imgs.xkcd.com/comics/python.png" height="525px" class="framed">
</a>

</div>

---

# Tour of Python: <strong class="gold">Scripting</strong>

<div class="font-large">

1. <strong class="info">Overview</strong>

2. <strong class="caution">Variables, Types, Expressions</strong>

3. <strong class="warning">Conditionals</strong>

4. <strong class="danger">Loops</strong>

5. <strong class="success">Functions</strong>

6. <strong class="special">Modules</strong>

</div>

---

# Example: [Fizz Buzz](https://github.com/nd-cse-20589-fa26/examples/blob/master/slides04/fizzbuzz.py)

> Write a program that prints the numbers from `1` to `100`. But for multiples
> of **three** print <strong class="danger">"Fizz"</strong> instead of the
> number and for the multiples of **five** print <strong
> class="danger">"Buzz"</strong>. For numbers which are multiples of both
> **three** and **five** print <strong class="danger">"FizzBuzz"</strong>.

<br>

<div class="centered">

<img src="https://storage.ghost.io/c/eb/aa/ebaa2665-01a8-4415-8825-69d1f0e8fd19/content/images/size/w320/2025/01/coding-horror-logo-transparency.png" height="200px">

[Why Can't Programmers... Program?](https://blog.codinghorror.com/why-cant-programmers-program/) -- [Jeff Atwood](https://en.wikipedia.org/wiki/Jeff_Atwood)

</div>

