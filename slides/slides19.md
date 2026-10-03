---
title: "Slides 19: Signals"
description: "Signals"
author: Peter Bui
keywords: lecture,sos,signals
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides19.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Signals

---

# Questions

<div class="font-large">

1. What is a <strong class="danger">signal</strong>?

2. What <strong class="warning">system calls</strong> can we use with <strong
   class="success">signals</strong>?

</div>

---

# Signals: <span class="gold">Overview</span>

<strong class="special">Signals</strong> are a means of notifying a
<strong class="success">process</strong> of an **event**.

- Each <strong class="special">signal</strong> delivers a <strong
  class="danger">small integer</strong> that represents a particular **event**.

- To deliver the **event**, the <strong class="caution">kernel</strong> will **interrupt**
  the normal execution of the target <strong class="success">process</strong>.

- To catch particular **events** and perform custom actions, <strong
  class="success">processes</strong> can register callback functions (ie.
  *handlers*) for certain **events**.

- After the *handlers* are executed, the <strong class="success">process</strong> will
  continue executing where it was interrupted.

---

# Signals: <span class="gold">Kill / Signal</span>

<div class="columns">

<div class="margin-top-0-5">

## <strong class="info">Kill</strong>

To send a signal to a process, use [kill].

```python
# Send SIGTERM to process with
# specified PID
os.kill(pid, signal.SIGTERM)
```

</div>

<div class="margin-top-0-5">

## <strong class="info">Signal</strong>

To **register** a <strong class="special">callback function</strong> for a
particular **event**, use [signal].

```python
# Register handler for SIGINT
signal(signal.SIGINT, handler)

# Handle SIGINT event
def handler(signum, frame):
    print("Can't stop! Won't stop!")
```

[kill]: https://docs.python.org/3/library/os.html#os.kill
[signal]: https://docs.python.org/3/library/signal.html#module-signal

</div>

</div>

---

# Signals: <span class="gold">SIGCHLD / SIGALRM</span>

<div class="columns">

<div class="margin-top-0-5">

## <strong class="special">SIGCHLD</strong>

A <strong class="special">SIGCHLD</strong> **event** is delivered to the
<strong class="success">process</strong> whenever one of its <strong
class="warning">child</strong> <strong class="success">processes</strong> has
terminated.


```python
# Register handler for SIGCHLD
signal.signal(signal.SIGCHLD, handler)

# Handle SIGCHLD event
def handler(signum, frame):
    print('Waiting for terminated child')
    os.wait()
```

</div>

<div class="margin-top-0-5">

## <strong class="special">SIGARLM</strong>

A <strong class="special">SIGALRM</strong> **event** can be scheduled for the
future using [alarm] or [setitimer].

```python
# Register handler for SIGCHLD
signal.signal(signal.SIGALRM, handler)

# Schedule one time alarm in 5 seconds
signal.alarm(5)

# Handle SIGCHLD event
def handler(signum, frame):
    signal.alarm(0) # Disable previous alarm
```

</div>

</div>

[alarm]: https://docs.python.org/3/library/signal.html#signal.alarm

---

# Signals: <span class="gold">Examples</span>

<div class="font-large">

1. [fork_bomb.py]: Demonstrates <strong
   class="danger">denial-of-service</strong> attack where a program <strong
   class="warning">recursively replicates</strong> itself to consume <strong
   class="info">system resources</strong>.

2. [zombies.py]: Demonstrates situation where the **child** <strong
   class="success">process</strong> has terminated but the **parent** <strong
   class="success">process</strong> has not <strong
   class="warning">waited</strong> for it yet.

3. [alarm.py]: Demonstrates <strong class="warning">killing</strong> a child
   <strong class="success">process</strong> after an [alarm] is triggered.

</div>

[fork_bomb.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides19/fork_bomb.py
[zombies.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides19/zombies.py
[alarm.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides19/alarm.py
