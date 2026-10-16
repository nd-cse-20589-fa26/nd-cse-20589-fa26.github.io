---
title: "Slides 20: Environments"
description: "Environments"
author: Peter Bui
keywords: lecture,sos,venv,environments
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides20.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Environments

---

# Questions

<div class="font-large">

1. How do you create a <strong class="success">Python</strong> <strong
   class="info">environment</strong>?

2. How do install <strong class="success">Python</strong> <strong
   class="warning">packages</strong> inside a <strong
   class="info">environment</strong>?

</div>

---

# Environments: <span class="gold">Overview</span>

A <strong class="success">Python</strong> <strong class="info">virtual
environment</strong> (ie. `venv`) is a way to create an <strong
class="danger">isolated</strong> workspace for your **project** and its
**dependencies**.

- Does not require **root** permisions.

- Allows you to change **interpreters**.

- Allows you to install different **libraries**.

---

# Environments: <span class="gold">Creation</span>

To create a <strong class="info">virtual environment</strong>, go to your
**project** directory and run:

```bash
# Create virtual environment in .venv directory
$ python3 -m venv .venv

# List contents of virtual environment
$ ls .venv
bin/  include/  lib/  lib64@  pyvenv.cfg
```

This will download and install a <strong class="success">Python</strong>
run-time into the `.venv` directory (*same version*).

---

# Environments: <span class="gold">Activation</span>

To activate the <strong class="info">virtual environment</strong>, `source` the
provided `.venv/bin/activate` script:

```bash
# Activate virtual environment
$ source .venv/bin/activate
```

This will modify your **shell prompt** by adding a `(.venv)` to the end of
`PS1`.

```bash
# Deactivate virtual environment
$ deactivate
```

---

# Environments: <span class="gold">Installation</span>

To install packages in the <strong class="info">virtual environment</strong>,
use the `pip` command:

```bash
# Install requests library
$ pip install requests

# Upgrade pip library
$ pip install --upgrade pip
```

The `pip` command will download and install the libraries to the
`.venv/lib/pythonX.YZ/site-packages/` folder (*where `X.YZ` is the version
number*).

---

# Example: [curl_all.py]

> Write a program that downloads all `URLs` to separate files.

1. Use `requests` instead of `os.popen`.
2. Use [tqdm] to show progress.
3. Use [concurrent.futures] for concurrency.

[curl_all.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides20/curl_all.py
[tqdm]: https://tqdm.github.io/
[concurrent.futures]: https://docs.python.org/3/library/concurrent.futures.html


