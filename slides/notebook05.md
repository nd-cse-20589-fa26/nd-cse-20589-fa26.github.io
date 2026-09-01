---
title: "Notebook 05: Data Structures, Arguments, I/O"
description: "Data Structures, Arguments, I/O"
author: Peter Bui
keywords: notebook,sos,python,data structures, arguments, i/o
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/notebook05.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Data Structures, Arguments, I/O

---

<div class="slide-centered">

<img src="static/img/notebook05-zen-of-python.png" height="675px">

</div>

---

# Tour of Python: <strong class="gold">Scripting</strong>

<div class="font-large">

1. <strong class="success">Functions</strong>

2. <strong class="special">Modules</strong>

3. <strong class="danger">Tests</strong>

4. <strong class="caution">Data Structures</strong>

5. <strong class="warning">Arguments</strong>

6. <strong class="comment">I/O</strong>

</div>

---

# Example: [Fizz Buzz](https://github.com/nd-cse-20589-fa26/examples/blob/master/slides05/fizzbuzz.py)

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

---

# Example: [Anagrams](https://github.com/nd-cse-20589-fa26/examples/blob/master/slides05/anagram.py)

> Given two words, determine if they are [anagrams].

```bash
$ ./anagram.py -i       # Ignore case
listen silent
ANAGRAM!
army Mary
ANAGRAM!
card dare
NOT ANAGRAM!
```

[anagrams]: https://en.wikipedia.org/wiki/Anagram

---

# Data Structures: <span class="gold">Summary</span>

<div class="slide-centered">

<table class="bordered">
<thead>
    <th>Container</th>
    <th>C</th>
    <th>Python</th>
    <th>Python Syntax</th>
</thead>
<tbody>
    <tr class="success-bg" height="100px">
        <td class="centered" width="300px" height="100px">&nbsp;<br>&nbsp;</td>
        <td class="centered" width="300px"></td>
        <td class="centered" width="300px"></td>
        <td class="centered" width="300px"></td>
    </tr>
    <tr class="caution-bg" height="100px">
        <td class="centered" width="300px" height="100px">&nbsp;<br>&nbsp;</td>
        <td class="centered"></td>
        <td class="centered"></td>
        <td class="centered"></td>
    </tr>
    <tr class="warning-bg" height="100px">
        <td class="centered" width="300px" height="100px">&nbsp;<br>&nbsp;</td>
        <td class="centered"></td>
        <td class="centered"></td>
        <td class="centered"></td>
    </tr>
    <tr class="danger-bg" height="100px">
        <td class="centered" width="300px" height="100px">&nbsp;<br>&nbsp;</td>
        <td class="centered"></td>
        <td class="centered"></td>
        <td class="centered"></td>
    </tr>
</tbody>
</table>

</div>
