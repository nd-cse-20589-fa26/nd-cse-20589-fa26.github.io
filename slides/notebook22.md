---
title: "Notebook 22: Directories"
description: "Directories"
author: Peter Bui
keywords: notebook,sos,system calls,directories
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/notebook22.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Directories

---

# Directories: <span class="gold">Overview</span>

As with <strong class="success">files</strong>, <strong
class="caution">directories</strong> are also represented by <strong
class="special"> ________________</strong>

in the <strong class="warning"> __________________</strong>.

<br>

- Each <strong class="caution">directory</strong> contains:

    - References to <b> _____________________________________________</b>

    - References to <b> _____________________________________________</b>

    <br>

- Each <strong class="success">process</strong> tracks its
  <strong class="caution"> ______________________________________</strong>.

---

# Directories: <span class="gold">Operations</span>

Many of the <strong class="warning">file system</strong> operations we might
use <strong class="danger">unix commands</strong> for can be accomplished with
<strong class="success">Python</strong> functions:

<table class="bordered">
<thead>
    <th class="info-bg">Unix Command</th>
    <th class="success-bg">Python Function</th>
</thead>
<tbody>
<tr>
    <td class="info-bg">cd</td>
    <td class="success-bg">os.chdir(path)</td>
</tr>
<tr>
    <td class="info-bg">chmod</td>
    <td class="success-bg">os.chmod(path, mode)</td>
</tr>
<tr>
    <td class="info-bg">mkdir</td>
    <td class="success-bg">os.mkdir(path, mode)</td>
</tr>
<tr>
    <td class="info-bg">rm</td>
    <td class="success-bg">os.unlink(path)</td>
</tr>
<tr>
    <td class="info-bg">mv</td>
    <td class="success-bg">os.rename(path)</td>
</tr>
<tr>
    <td class="info-bg">cp</td>
    <td class="success-bg">shutil.copy(src, dst)</td>
</tr>
</tbody>
</table>

---

# Directories: [list_rec.py] (<i class="muted">Recursive</i>)

> Write a simplified version of [ls] that lists the files in directory
> (*possibly recursively*) along with the corresponding file sizes.

```
$ ./list_rec.py  -h
Usage: list [directory]
    -R      List the contents of all directories recursively
```

[ls]: https://man7.org/linux/man-pages/man1/ls.1.html

[list_rec.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides22/list_rec.py

---

# OOP: <span class="gold">Inheritance</span>

<strong class="warning"> __________________________</strong> is a core <strong
class="special">OOP principle</strong> that enables the

creation of <strong class="caution"> _____________________________</strong>
between units to allow for

<strong class="success"> _______________________________</strong>.

<br>
<br>

<div class="alert info-bg">

<br>To define an <strong class="special"> _____________________________</strong>, we can
create an [abstract base class] and mark [abstract methods] which need to be

defined by <strong class="caution"> ______________________</strong> that <strong
class="special">inherit</strong> from this `ABC`.

</div>

[abstract base class]: https://docs.python.org/3/library/abc.html
[abstract methods]: https://docs.python.org/3/library/abc.html#abc.abstractmethod

---

# OOP: <span class="gold">Factory Pattern</span>

The <strong class="special">factory design pattern</strong> uses a specialized
<strong class="special"> ______________________</strong> method that produces **instantiated**
objects.  This is done to <strong class="success">abstract</strong> away
complex object instantiation logic.

- <strong class="caution"> __________________________</strong>: An interface or
  abstract class shared by all objects the **factory** produces.

- <strong class="warning"> __________________________</strong>: Specific classes
  that implement <strong class="caution">product</strong> interface.

- <strong class="danger">  __________________________</strong>: Specific <strong
  class="special">factory</strong> method that returns <strong
  class="warning">concrete products</strong>.
