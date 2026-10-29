---
title: "Notebook 23: I/O"
description: "I/O"
author: Peter Bui
keywords: notebook,sos,system calls,i/o
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/notebook23.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## I/O

---

# I/O: <span class="gold">Overview</span>

<div class="columns">

<div>

All <strong class="warning">input</strong> and <strong
class="warning">output</strong> is performed

on <strong class="success"> ___________________________</strong>:

1. <strong class="caution"> ___________________________</strong>

    Acquire handle to stream of data.

2. <strong class="caution"> ___________________________</strong>

    Release handle to stream of data.

</div>

<div>

3. <strong class="warning"> ___________________________</strong>

    Load chunk from stream of data.

4. <strong class="warning"> ___________________________</strong>

    Store chunk to stream of data.

5. <strong class="danger">  ___________________________</strong>

    Move within stream of data.

</div>

</div>

---

# I/O: [copy_file.py]

> Write a simplified version of [cp] that copies one file to another.

```bash
# Copy /etc/hosts to hosts.copy
$ ./copy_file.py /etc/hosts hosts.copy

# Verify that sha1sums are the same
$ sha1sum /etc/hosts hosts.copy
```

[cp]: https://man7.org/linux/man-pages/man1/cp.1.html
[copy_file.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides23/copy_file.py

---

# I/O: [file_array.py]

> Create a **persistent array** that supports the **index** operator.

```python
# Create Persistent Array
array = FileArray('array.txt')

# Write to Persistent Array
for index, char in enumerate('hello, world'):
    array[index] = char.encode()

# Write to Persistent Array (again)
for index, char in enumerate('goodbye, all'):
    array[(1<<8) + index] = char.encode()
```

[file_array.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides23/file_array.py
