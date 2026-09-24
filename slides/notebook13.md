---
title: "Notebook 13: Sorting"
description: "Sorting"
author: Peter Bui
keywords: notebook,sos,sorting
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/notebook13.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Sorting

---

# Filters: <span class="gold">Transformers / Selectors</span>

<br>

<table class="bordered">
<thead>
    <th>Filter</th>
    <th>Python Analog</th>
</thead>
<tbody>
<tr class="info-bg">
    <td class="centered"><b>tr</b></td>
    <td width="900px"><br><br></td>
</tr>
<tr class="success-bg">
    <td class="centered"><b>cut/awk</b></td>
    <td width="900px"><br><br></td>
</tr>
<tr class="warning-bg">
    <td class="centered"><b>grep</b></td>
    <td width="900px"><br><br></td>
</tr>
<tr class="danger-bg">
    <td class="centered"><b>sed</b></td>
    <td width="900px"><br><br></td>
</tr>
</tbody>
</table>

---

# Filters: <span class="gold">Aggregators</span>

<br>

<table class="bordered">
<thead>
    <th>Filter</th>
    <th>Python Analog</th>
</thead>
<tbody>
<tr class="info-bg">
    <td class="centered"><b>head</b></td>
    <td width="900px"><br><br></td>
</tr>
<tr class="success-bg">
    <td class="centered"><b>tail</b></td>
    <td width="900px"><br><br></td>
</tr>
<tr class="warning-bg">
    <td class="centered"><b>wc</b></td>
    <td width="900px"><br><br></td>
</tr>
<tr class="danger-bg">
    <td class="centered"><b>uniq</b></td>
    <td width="900px"><br><br></td>
</tr>
</tbody>
</table>

---

# Example: [cse-curriculum.py]

<div class="font-large">

Given the [Computer Science Curriculum](https://cse.nd.edu/undergraduate/computer-science-curriculum-fall-2025-beyond/) (<i>[yld.me/mbfL](https://yld.me/mbfL)</i>):

1. How many `MATH` vs `PHYS` vs `CSE` courses?

2. How many sophomore `CSE` courses?

</div>

[cse-curriculum.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides12/cse-curriculum.py

---

# Sorting: <span class="gold">Overview</span>

To <strong class="danger">order</strong> a <strong
class="caution">sequence</strong> of values in <strong
class="success">Python</strong>, we can use the
<strong> ________</strong>
function on the <strong class="caution">sequence</strong> to get a new [list].

<br>

<div class="columns-2-1">

<div>

- <strong> ____________________________________</strong>

    <br>

- <strong> ____________________________________</strong>

    <br>

- <strong> ____________________________________</strong>

    <br>

</div>

<div>

<div class="alert success-bg">

[ ] **In-Place**
<br>
<br>[ ] **Reverse**
<br>
<br>[ ] **Key**, [lambda]
<br>
<br>[ ] **Multi-factor**
<br>
<br>[ ] **Min**, **Max**

</div>

</div>

</div>

[sorted]: https://docs.python.org/3/builtins/functions.html#sorted
[list]: https://docs.python.org/3/builtins/stdtypes.html#typesseq-list
[merge sort]: https://en.wikipedia.org/wiki/Merge_sort
[insertion sort]: https://en.wikipedia.org/wiki/Insertion_sort
[TimSort]: https://en.wikipedia.org/wiki/Timsort
[stable]: https://en.wikipedia.org/wiki/Category:Stable_sorts
[lambda]: https://docs.python.org/3/reference/expressions.html#lambda

