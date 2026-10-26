---
title: "Slides 21: Files"
description: "System Calls, Files"
author: Peter Bui
keywords: lecture,sos,system calls,files
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides21.html
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

<!-- _class: lead -->

# System Calls

---

# System Calls: <span class="gold">House of Cards</span>

<div class="slide-centered">
    <img src="static/img/slides18-house-of-cards.svg">
</div>

---

# System Calls: <span class="gold">Overview</span>

A <strong class="info">system call</strong> occurs when a <strong
class="success">user application</strong> requests a <strong
class="warning">service, operation, or resource</strong> from the <strong
class="danger">operating system kernel</strong>.

<div class="columns-1-2">

<div class="font-small">

- <strong class="caution">Process control</strong>

    - fork/exec/wait
    - kill/signal

- <strong class="caution">File manipulation</strong>

    - stat
    - access

- <strong class="caution">I/O operations</strong>

    - open/close
    - read/write

- <strong class="caution">Network communication</strong>

    - socket
    - listen/bind
    - connect

</div>

<div class="centered middled">

<img src="static/img/slides21-system-call.svg">

</div>

</div>

---

# System Calls: <span class="gold">Strace</span>

We can trace the <strong class="info">system calls</strong> used by a program
by using [strace]:

<div class="columns">

<div>

```bash
# Trace all system calls
$ strace ls

# Trace an existing process
$ strace -p pid

# Only trace open system calls
$ strace -e open ls

# Get table of counts
$ strace -c ls
```

</div>

<div class="centered middled">

<img src="https://www.brendangregg.com/Slides/LinuxConNA2014_LinuxPerfTools/LinuxConNA2014_LinuxPerfTools_048.jpg" class="framed" width="600px">

</div>

</div>

[strace]: https://man7.org/linux/man-pages/man1/strace.1.html

---

<!-- _class: lead -->

# Files

---

# Files: <span class="gold">OS</span>

Many <strong class="primary">functions</strong> and <strong class="info">system
calls</strong> related to the <strong class="warning">file system</strong> are
provided by the [os] library:

```python
# Import OS library
>>> import os

# Create a path by joining directory and file name
>>> os.path.join(os.curdir, 'README.md')
'./README.md'

# Check if path exists
>>> os.path.exists('/etc/hosts')
True
```

[os]: https://docs.python.org/3/library/os.html

---

# Files: <span class="gold">Inodes</span>

<strong class="success">Files</strong> are objects stored on a <strong
class="warning">file system</strong>, which is usually a <strong
class="special">tree-like data structure</strong> managed by the <strong
class="caution">operating system</strong> to ensure data <strong
class="danger">persists</strong>.

<div class="columns">

<div class="centered middled">

<img src="static/img/slides03-files-inode.svg">

</div>

<div>

To keep track of <strong class="success">files</strong>, the <strong
class="caution">operating system</strong> stores information about each <strong
class="success">file</strong> in an <strong class="special">inode</strong>
structure in the <strong class="warning">file system</strong>.

<div class="font-smaller">

- Permissions
- Owner, Group
- File Size
- Links
- Timestamps

</div>

</div>

</div>

---

# Files: <span class="gold">stat</span>

To access the <strong class="special">inode</strong> information for a
<strong class="success">file</strong>, we can use the [os.stat] function:

```python
try:
    inode = os.stat(path)                       # Get inode information
    if stat.S_ISREG(inode.st_mode):             # Check if regular file
        print(f'{path} size: {inode.st_size}')  # Print file size
except OSError as e:
    print(e, file=sys.stderr)
```

To interpret some of these attributes, we can use the constants and functions
from [stat].  That said, we can often avoid doing this manually by using the
helper functions provided by <strong class="success">Python</strong>.

[os.stat]: https://docs.python.org/3/library/os.html#os.stat
[stat]: https://docs.python.org/3/library/stat.html

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

# Files: <span class="gold">Properties</span>

<strong class="success">Python</strong> also provides a number of useful
functions for getting the <strong class="info">properties</strong> of <strong
class="success">files</strong>.

<table class="bordered">
<thead>
    <th class="info-bg">Information</th>
    <th class="success-bg">Python Function</th>
</thead>
<tbody>
<tr>
    <td class="info-bg">Absolute Path</td>
    <td class="success-bg">os.path.abspath(path)</td>
</tr>
<tr>
    <td class="info-bg">Normalized Path</td>
    <td class="success-bg">os.path.normpath(path)</td>
</tr>
<tr>
    <td class="info-bg">File Name</td>
    <td class="success-bg">os.path.basename(path)</td>
</tr>
<tr>
    <td class="info-bg">Directory Name</td>
    <td class="success-bg">os.path.dirname(path)</td>
</tr>
<tr>
    <td class="info-bg">File Size</td>
    <td class="success-bg">os.path.getsize(path)</td>
</tr>
<tr>
    <td class="info-bg">File Extension</td>
    <td class="success-bg">os.path.splitext(path)[-1]</td>
</tr>
</tbody>
</table>

[test]: https://man7.org/linux/man-pages/man1/test.1.html

---

# Files: <span class="gold">Path</span>

In recent versions of <strong class="success">Python</strong>, the [pathlib]
library provides a <strong class="special">object-oriented</strong> wrapper to
many of the lower level [os] functions:

```python
>>> from pathlib import Path                # Load Path class from pathlib library

>>> path = Path('/etc/hosts')               # Create Path instance

>>> path.name                               # Get path name
'hosts'

>>> path.parent                             # Get path directory
PosixPath('/etc')

>>> path.stat().st_size                     # Get path size from stat structure
449
```

[pathlib]: https://docs.python.org/3/library/pathlib.html

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
