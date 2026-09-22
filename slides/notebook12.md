---
title: "Notebook 12: Filters"
description: "Filters"
author: Peter Bui
keywords: notebook,sos,filters
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/notebook12.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Filters

---

# Filters: <span class="gold">Overview</span>

<strong class="danger">Unix</strong> includes many utilities that perform the
following:

<br>

<div class="centered">

<img src="static/img/slides11-pipeline.svg">

</div>

1. <strong class="info"> ____________________________________________________________</strong>

    <br>

2. <strong class="success"> ____________________________________________________________</strong>

    <br>

3. <strong class="caution"> ____________________________________________________________</strong>

---

# Filters: <span class="gold">Transformers / Selectors</span>

<br>

<table class="bordered">
<thead>
    <th>Filter</th>
    <th>Description</th>
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

# Example: [tmnt.py]

Given the file `tmnt.txt`, which contains:

```
Leonardo      blue    katana
Donatello     purple  bo
Raphael       red     sai
Michelangelo  orange  nunchucks
```

1. List only the **colors** of the turtles.

2. List only the **turtles** whose names end in lo.

3. List the **weapons** that don't end with a vowel.

[tmnt.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides12/tmnt.py

---

# Filters: <span class="gold">Aggregators</span>

<br>

<table class="bordered">
<thead>
    <th>Filter</th>
    <th>Description</th>
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
