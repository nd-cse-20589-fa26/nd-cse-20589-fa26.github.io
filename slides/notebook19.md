---
title: "Notebook 19: Signals"
description: "Signals"
author: Peter Bui
keywords: notebook,sos,signals
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/notebook19.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Signals

---

# Review: <span class="gold">Process Life Cycle</span>

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

---

# Signals: <span class="gold">Event-based Programming</span>

<strong class="special">Signals</strong> are a means of notifying a
<strong class="success"> ___________</strong> of an
<strong> __________</strong>.

<div class="columns-2-1">

<div>

<br>

- <strong> _____________________________________</strong>

    <br>

- <strong> _____________________________________</strong>

    <br>

- <strong> _____________________________________</strong>

    <br>

- <strong> _____________________________________</strong>

</div>

<div class="middled centered">
<br>
<img src="static/img/slides19-event-loop.svg" height="300px">
</div>

</div>

---

# Signals: <span class="gold">Examples</span>

<div class="font-large">

1. [fork_bomb.py]

    <strong> ________________________________________________</strong>

    <br>

2. [zombies.py]

    <strong> ________________________________________________</strong>

    <br>

3. [alarm.py]:

    <strong> ________________________________________________</strong>

</div>

[fork_bomb.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides19/fork_bomb.py
[zombies.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides19/zombies.py
[alarm.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides19/alarm.py
