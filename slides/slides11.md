---
title: "Slides 11: Pipelines"
description: "Pipelines"
author: Peter Bui
keywords: lecture,sos,pipelines
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides11.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Pipelines

---

# Pipelines: <span class="gold">Unix Philosopy</span>

<div class="slide-centered font-large">

Write programs that <strong class="caution">do one thing</strong> and <strong
class="caution">do it well</strong>.

Write programs that <strong class="caution">work together</strong>.

Write programs that <strong class="caution">handle text streams</strong>,
because that is a universal interface.

</div>

---

# Pipelines: <span class="gold">Assembly Line</span>

A Unix <strong class="primary">pipeline</strong> is a <strong
class="special">computational assembly line</strong> where the output of one
<strong class="success">process</strong> is fed to the next <strong
class="success">process</strong>:

<div class="centered">

<br>

<img src="static/img/slides11-pipeline.svg">

</div>

- Each <strong class="success">process</strong> focuses with a <strong
  class="caution">single operation</strong>.

- Each <strong class="caution">operation</strong> performs an <strong
  class="warning">action</strong> on the previous input.

- Each <strong class="caution">operation</strong> is <strong
  class="success">independent</strong> and can be <strong
  class="success">combined</strong> in different ways.

---

# Pipelines: <span class="gold">Powerful Pattern</span>

The <strong class="primary">pipeline pattern</strong> is found throught <strong
class="success">computing science</strong> and <strong
class="success">engineering</strong>:

<div class="centered">

<br>

<img src="static/img/slides11-pipeline-cpu.svg">

<br>
<br>

<img src="static/img/slides11-pipeline-gpu.svg">

</div>

<br>

<div class="centered">

<i>Computational <strong class="primary">pipelines</strong> allow
for<br><strong class="special">specialization</strong>, <strong
class="warning">debugging</strong>, <strong class="caution">extension</strong>
and <strong class="success">concurrency</strong>.</i>

</div>

---

# Pipelines: <span class="gold">subprocess</span>

In <strong class="success">Python</strong>, we can create a <strong
class="primary">pipeline</strong> by using functions from the [subprocess]
module to *chain* <strong class="warning">proceses</strong>:

```python
from subprocess import Popen, PIPE, DEVNULL, run

ps   = Popen(['ps', 'aux'], stdout=PIPE, stderr=DEVNULL)
grep = Popen(['grep', 'pbui'], stdin=ps.stdout, stdout=PIPE)
wc   = run(['wc', '-l'], stdin=grep.stdout, stdout=PIPE)

print(wc.stdout.decode(), end='')
```

[subprocess]: https://docs.python.org/3/library/subprocess.html

---

# Pipelines: <span class="gold">Demonstration</span> (<i class="muted">1</i>)

> How many `bash` <strong class="success">processes</strong> are on there on
> <strong class="info">student10.cse.nd.edu</strong>?

<div class="columns">

<div>

```python
# Python Solution

count = 0
for line in os.popen('ps aux'):
    if 'bash' in line:
        count += 1
print(count)
```

</div>

<div>

```bash
# Pipeline Solution

ps aux | grep -v grep | grep bash \
       | wc -l
```

</div>

</div>

---

# Pipelines: <span class="gold">Demonstration</span> (<i class="muted">2</i>)

> How many different users <strong class="success">processes</strong> are on there on
> <strong class="info">student10.cse.nd.edu</strong>?

<div class="columns">

<div>

```python
# Python Solution

users = set()
for line in os.popen('ps aux'):
    user = line.split()[0]
    users.add(user)

print(len(users))
```

</div>

<div>

```bash
# Pipeline Solution

ps aux | awk '{print $1}' \
       | sort | uniq \
       | wc -l
```

</div>

</div>

---

# Pipelines: <span class="gold">Demonstration</span> (<i class="muted">3</i>)

> Who has the most <strong class="success">processes</strong> on
> <strong class="info">student10.cse.nd.edu</strong>?

<div class="columns">

<div>

```python
# Python Solution

counts = {}
for line in os.popen('ps aux'):
    user = line.split()[0]
    counts[user] = counts.get(user, 0) + 1

max_user = None
for user, count in counts.items():
    if count > counts.get(max_user, 0):
        max_user = user

print(max_user)
```

</div>

<div>

```bash
# Pipeline Solution

ps aux | awk '{print $1}' \
       | sort | uniq -c \
       | sort -rn | head -n 1 \
       | awk '{print $2}'
```

</div>

</div>
