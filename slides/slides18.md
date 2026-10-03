---
title: "Slides 18: Processes"
description: "Processes"
author: Peter Bui
keywords: lecture,sos,processes
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides18.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Processes

---

# Questions

<div class="font-large">

1. What is a <strong class="success">process</strong>?

2. What <strong class="info">system calls</strong> can we use with <strong
   class="success">processes</strong>?

</div>

---

# Process: <span class="gold">Overview</span>

<div class="columns-2-1">

<div>

A <strong class="success">process</strong> is a **loaded** instance of a
program; it is a unit of <strong class="warning">allocation</strong>
(*resources*, *privileges*, etc.).

- <strong class="success">Memory Address Space</strong>: code, data, heap,
  stack.

- <strong class="caution">Kernel State</strong>: permissions, file descriptors,
  etc.

- <strong class="info">Execution Context</strong>: program counter, stack
  pointer, data registers.

</div>

<div class="slide-centered">

<img src="static/img/slides18-process-machine-state.svg" width="300">

</div>

</div>

---

# Process: <span class="gold">Life Cycle</span>

<div class="columns-2-3">

<div class="font-smaller">

1. <strong class="success">Parent process</strong> [forks] to create a new
   <strong class="warning">child process</strong>.

2. <strong class="warning">Child process</strong> performs actions, possible
   [execs] to run another program.

3. <strong class="success">Parent process</strong> [waits] for <strong
   class="warning">child process</strong>.

4. <strong class="warning">Child process</strong> [exits].

5. <strong class="success">Parent process</strong> receives <strong
   class="special">status code</strong> of <strong class="warning">child
   process</strong>.

</div>

<div class="slide-centered margin-top-0-5">

<img src="static/img/slides18-process-life-cycle.svg" width="750">

</div>

</div>

[forks]: https://docs.python.org/3/library/os.html#os.fork
[execs]: https://docs.python.org/3/library/os.html#os.execvp
[waits]: https://docs.python.org/3/library/os.html#os.wait
[exits]: https://docs.python.org/3/library/sys.html#sys.exit

---

# Process: <span class="gold">Fork</span>

[fork] creates a new <strong class="warning">child process</strong> based off
the <strong class="special">machine state</strong> of the current <strong
class="success">parent process</strong>.

<div class="columns">

<div>

```python
try:
    pid = os.fork()
except OSError:
    # Handle Error

if pid == 0:
    # Child Process
else:
    # Parent
```

</div>

<div class="margin-top-0-5">

<div class="alert success-bg">

After a **successful** [fork], there are two **distinct** <strong
class="success">processes</strong> which have the **same** <strong
class="danger">code</strong>, but **different**:

- <strong class="success">Memory Address Space</strong>

- <strong class="caution">Kernel State</strong>

- <strong class="info">Execution Context</strong>

</div>

</div>

</div>

[fork]: https://docs.python.org/3/library/os.html#os.fork

---

# Process: <span class="gold">Exec</span>

[exec] replaces the <strong class="danger">code</strong> in the <strong
class="success">address space</strong> of the current <strong
class="success">process</strong> and resets the <strong class="info">execution
context</strong>.

<div class="columns-3-2">

<div>

```python
argv = ['ls', '-l']     # Command to run
pid  = os.fork()        # Create child process

if pid == 0:            # Child process
    try:                # Execute command
        os.execvp(argv[0], argv)
    except OSError:
        sys.exit(1)     # Exit if exec fails
```

</div>

<div class="margin-top-0-5">

<div class="alert info-bg font-smaller">

[exec] is actually a family of **functions** which differ in how they expect
the **command** is passed to the function, whether or not to search the
**PATH**, or whether or not to include a custom **environment array**:

- [execl], [execlp], [execlpe]
- [execv], [execvp], [execvpe]

</div>

</div>

</div>

[exec]: https://docs.python.org/3/library/os.html#os.execvp
[execl]: https://docs.python.org/3/library/os.html#os.execl
[execlp]: https://docs.python.org/3/library/os.html#os.execlp
[execlpe]: https://docs.python.org/3/library/os.html#os.execlpe
[execv]: https://docs.python.org/3/library/os.html#os.execv
[execvp]: https://docs.python.org/3/library/os.html#os.execvp
[execvpe]: https://docs.python.org/3/library/os.html#os.execvpe

</div>

---

# Process: <span class="gold">Wait / Exit</span>

<div class="columns">

<div class="margin-top-0-5">

## <strong class="info">Wait</strong>

[wait] suspends <strong class="success">process</strong> until one of its
<strong class="warning">children</strong> has terminated and retrieves its
<strong class="special">status code</strong>.

```python
try:
    pid, status = os.wait()
except OSError:
    # Handle Error
```

</div>

<div class="margin-top-0-5">

## <strong class="info">Exit</strong>

[exit] terminates a <strong class="success">process</strong> and sets its
<strong class="special">status code</strong>.

```python
# Exit without cleanup
os._exit(1)

# Cleanup and exit
sys.exit(1)
```

[wait]: https://docs.python.org/3/library/os.html#os.wait
[exit]: https://docs.python.org/3/library/sys.html#sys.exit

</div>

</div>

<br>

<div class="alert warning-bg centered">

The `status` returned from [wait] is a **bitmask**.  To extract the actual
**exit code**, use `os.WEXITSTATUS(status)`.

</div>

---

# Processes: <span class="gold">Utilities</span>

<div class="columns">

<div>

We can execute a shell command by using [system]:


```python
# Execute ls -l
os.system('ls -l')
```

</div>

<div>

We can create a <strong class="caution">pipe</strong> to a command by using [popen]:

```python
# Execute and from ls -l
for line in os.popen('ls -l'):
    print(line.rstrip())
```

</div>

</div>

<br>

<div class="alert warning-bg centered font-smaller">

Both [system] and [popen] spawn a <strong class="primary">shell</strong>
to execute the given commands.  This means that these utility functions have
some extra overhead due to an additional <strong class="primary">shell</strong>
process.  However, the benefit of this approach is that users can do more
sophisticated commands such as <strong class="success">pipelines</strong>.

</div>

[system]: https://docs.python.org/3/library/os.html#os.system
[popen]: https://docs.python.org/3/library/os.html#os.popen

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
