---
title: "Notebook 21: Files"
description: "System Calls, Files"
author: Peter Bui
keywords: notebook,sos,system calls,files
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/notebook21.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Files

---

# Questions

<div class="font-large">

1. What is a <strong class="info">system call</strong>?

2. How do we lookup a file's <strong class="special">inode</strong> information?

</div>

---

# System Calls: <span class="gold">House of Cards</span>

<div class="slide-centered">
    <img src="static/img/slides18-house-of-cards-blank.svg">
</div>

---

# System Calls: <span class="gold">Overview</span>

A <strong class="info">system call</strong> occurs when a <strong
class="success"> _____________________________</strong> requests a

<strong class="warning">service, operation, or resource</strong> from the
<strong class="danger"> __________________________</strong>.

<div class="columns-1-2">

<div class="font-smaller">

- <strong class="caution">Process control</strong>

    <br>

- <strong class="caution">File manipulation</strong>

    <br>

- <strong class="caution">I/O operations</strong>

    <br>

- <strong class="caution">Network communication</strong>

    <br>

</div>

<div class="centered middled">

<img src="static/img/slides21-system-call.svg">

</div>

</div>

---

# Files: <span class="gold">Inodes</span>

<strong class="success">Files</strong> are objects stored on a <strong
class="warning"> ________________</strong>, which is usually a

<strong class="special">tree-like data structure</strong> managed by the <strong
class="caution">operating system</strong> to ensure

data <strong class="danger"> ______________</strong>.

<br>

<div class="centered middled">

<img src="static/img/slides03-files-inode-blank.svg">

</div>

---

# Files: <span class="gold">Test Equivalences</span>

The [test] command is used to check the <strong class="special">inode</strong>
of a <strong class="success">file</strong>.  We can perform similar checks
using <strong class="success">Python</strong> functions:

<table class="bordered">
<thead>
    <th class="info-bg">Test Command</th>
    <th class="success-bg">Python Function</th>
</thead>
<tbody>
<tr>
    <td class="info-bg">test -f</td>
    <td class="success-bg">os.path.isfile(path)</td>
</tr>
<tr>
    <td class="info-bg">test -d</td>
    <td class="success-bg">os.path.isdir(path)</td>
</tr>
<tr>
    <td class="info-bg">test -e</td>
    <td class="success-bg">os.path.exists(path)</td>
</tr>
<tr>
    <td class="info-bg">test -r</td>
    <td class="success-bg">os.access(path, os.R_OK)</td>
</tr>
<tr>
    <td class="info-bg">test -w</td>
    <td class="success-bg">os.access(path, os.W_OK)</td>
</tr>
<tr>
    <td class="info-bg">test -x</td>
    <td class="success-bg">os.access(path, os.X_OK)</td>
</tr>
</tbody>
</table>

[test]: https://man7.org/linux/man-pages/man1/test.1.html

---

# Files: [check.py]

> Write a program to check the properties of a file (ie. [test]).

```
$ ./check.py
Usage: check flag path
   -e path      Returns if path exists
   -r path      Returns if path is readable
   -x path      Returns if path is executable
   -d path      Returns if path is a directory
   -f path      Returns if path is a regular file
   -s path      Returns if path exists and has size greater than zero
```

[check.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides21/check.py
