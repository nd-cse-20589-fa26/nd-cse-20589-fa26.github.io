---
title: "Notebook 18: Processes"
description: "Processes"
author: Peter Bui
keywords: notebook,sos,processes
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/notebook18.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Processes

---

# Questions

<div class="font-large">

1. What is a <strong class="success">process</strong>?

2. What <strong class="warning">system calls</strong> can we use with <strong
   class="success">processes</strong>?

</div>

---

# Process: <span class="gold">Overview</span>

<div class="columns-2-1">

<div>

A <strong class="success">process</strong> is a
<strong> __________________________</strong>;

it is a unit of <strong class="warning"> _________________________</strong>.

- <strong class="success"> ___________________________________</strong>

    code, data, heap, stack

- <strong class="caution"> ___________________________________</strong>

    permissions, file descriptors, etc.

- <strong class="info">    ___________________________________</strong>

    program counter, stack pointer, data registers

</div>

<div class="slide-centered">

<br>

<img src="static/img/slides18-process-machine-state-blank.svg" width="300">

</div>

</div>

---

# Process: <span class="gold">System Calls</span>

A <strong class="info">system call</strong> occurs when a
<strong class="special">_________________________</strong> requests a

<strong class="warning">service or resource</strong> from the
<strong class="caution">_________________________</strong>.

<div class="centered">

<br>

<img src="static/img/slides18-house-of-cards-blank.svg">

</div>

---

# Process: <span class="gold">Life Cycle</span>

<div class="slide-centered">

<img src="static/img/slides18-process-life-cycle-blank.svg" width="750">

</div>

[forks]: https://docs.python.org/3/library/os.html#os.fork
[execs]: https://docs.python.org/3/library/os.html#os.execvp
[waits]: https://docs.python.org/3/library/os.html#os.wait
[exits]: https://docs.python.org/3/library/sys.html#sys.exit

---

# Example: [safe_system.py]

> Write a `SafeSystem` object that implements the <strong
> class="warning">context manager protocol</strong> to create a child <strong
> class="success">process</strong> that executes the given command while the
> parent <strong class="success">process</strong> runs.

```python
with SafeSystem(['ls', '-l']) as process:
    for i in range(10):
        time.sleep(0.1)
        print(f'{i}: {process.state}')

print(f'Final: {process.state}')
```

[safe_system.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides18/safesystem.py
