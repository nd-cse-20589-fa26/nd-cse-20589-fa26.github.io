---
title: "Slides 11: Filters"
description: "Filters"
author: Peter Bui
keywords: lecture,sos,filters
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides12.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Filters

---

# Filters: <span class="gold">Overview</span>

<strong class="danger">Unix</strong> includes many utilities that perform the
following:

1. <strong class="info">Read</strong> data from **standard input**.

2. <strong class="success">Perform</strong> some operation on the data.

3. <strong class="caution">Write</strong> results of operation to **standard output**.

<div class="centered">

<img src="static/img/slides11-pipeline.svg">

</div>

<div class="centered">

<i>We call these utilities <strong class="success">filters</strong> since they
**transform** their inputs in some manner.  Additionally, we can combine
multiple <strong class="success">filters</strong> together to form <strong
class="primary">pipelines</strong>.</i>

</div>

---

# Filters: <span class="gold">Tr</span>

[tr] allows us to **translate** from one set of characters to another set in a
stream of text.

<div class="columns">

<div>

```bash
# Shell

$ TEXT='burn this city'

# Translate from a to x, from b to y, from c to z
$ echo $TEXT | tr abc xyz
yurn this zity

# Uppercase all letters
$ echo $TEXT | tr a-z A-Z
BURN THIS CITY

# Delete all spaces
$ echo $TEXT | tr -d ' '
burnthiscity
```

</div>

<div>

```python
# Python

>>> text = 'burn this city'

# Translate from a to x, from b to y, from c to z
>>> text.translate(str.maketrans('abc', 'xyz'))
'yurn this zity'

# Uppercase all letters
>>> text.upper()
'BURN THIS CITY'

# Delete all spaces
>>> text.replace(' ', '')
'burnthiscity'
```

</div>

</div>

[tr]: https://man7.org/linux/man-pages/man1/tr.1.html

---

# Filters: <span class="gold">Cut / Awk</span>

[cut] and [awk] allow us to **extract** portions from each line in a stream of
text.

<div class="columns">

<div>

```bash
# Shell

$ TEXT='burn this city'

# Extract first field of each line
$ echo $TEXT | cut -d ' ' -f 1
$ echo $TEXT | awk '{print $1}'
burn

# Extract first and third fields of each line
$ echo $TEXT | cut -d ' ' -f 1,3
$ echo $TEXT | awk '{print $1, $3}'
burn city

# Extract 2nd through 4th characters of each line
$ echo $TEXT | cut -c 2-4
urn
```

</div>

<div>

```python
# Python

>>> text = 'burn this city'

# Extract first field of each line
>>> text.split()[0]
burn

# Extract first and third fields of each line
>>> ' '.join([text.split()[0], text.split()[2]])
'burn city'

# Extract 2nd through 4th characters of each line
>>> text[1:4]
urn
```

</div>

</div>


[cut]: https://man7.org/linux/man-pages/man1/cut.1.html
[awk]: https://man7.org/linux/man-pages/man1/awk.1.html

---

# Filters: <span class="gold">Grep</span>

[grep] allows us to **search** streams of text using <strong
class="success">regular expressions</strong>.

[grep]: https://man7.org/linux/man-pages/man1/grep.1.html

<div class="columns">

<div>

```bash
# Shell: Find all five letter words that
# begin with a or o and end with the same letter.

$ cat /usr/share/dict/words \
    | grep -E '^([ao]).{3}\1$'
aloha
alpha
ameba
aorta
arena
aroma
atria
outdo
outgo
```

</div>

<div>

```python
# Python: Find all five letter words that
# begin with a or o and end with the same letter.

path = '/usr/share/dict/words'
rx   = r'^([ao]).{3}\1$'

with open(path) as stream:
    for line in stream:
        if m := re.search(rx, line):
            print(m[0])
```

</div>

</div>


---

# Filters: <span class="gold">Sed</span>

[sed] allows us to **modify** streams of text using <strong
class="success">regular expressions</strong>.

[sed]: https://man7.org/linux/man-pages/man1/sed.1.html

<div class="columns">

<div>

```bash
# Shell: replace all numbers in IP address with
# a single x

$ cat /etc/hosts | sed -E 's/[0-9]{1,3}/x/g'
...
x.x.x.x weasel
x.x.x.x banshee
x.x.x.x xavier
x.x.x.x momo
```

</div>

<div>

```python
# Python: replace all numbers in IP address with
# a single x

path = '/etc/hosts'
rx   = r'[0-9]{1,3}'

with open(path) as stream:
    for line in stream:
        print(re.sub(rx, 'x', line), end='')
```

</div>

</div>

---

# Example: [tmnt.py]

Given the file `tmnt.txt`, which contains:

```
Leonardo      blue    katana
Donatello     purple  bo
Raphael       red     sai
Michelangelo  orange  nunchucks
```

1. List only the **colors** of the turtles.

2. List only the **turtles** whose names end in lo.

3. List the **weapons** that don't end with a vowel.

[tmnt.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides12/tmnt.py

---

# Filters: <span class="gold">Aggregators</span>

Some <strong class="danger">Unix</strong> utilities act as <strong
class="special">aggregators</strong> in that they collect and summarize the
data in some fashion.

<div class="columns">

<div>

```bash
# Shell

# List first three lines of /etc/hosts
$ cat /etc/hosts | head -n 3

# List last three lines of /etc/hosts
$ cat /etc/hosts | tail -n 3

# Print total number of lines in /etc/hosts
$ cat /etc/hosts | wc -l

# Print total number of unique lines in /etc/hosts
$ cat /etc/hosts | sort | uniq | wc -l
```

</div>

<div>

```python
# Python

>>> with open('/etc/hosts') as stream:
        lines = stream.readlines()

# List first three lines of /etc/hosts
>>> ''.join(lines[:3]

# List last three lines of /etc/hosts
>>> ''.join(lines[-3:])

# Print total number of lines in /etc/hosts
>>> len(lines)

# Print total number of unique lines in /etc/hosts
>>> len(set(lines))
```

</div>

</div>

---

# Example: [cse-curriculum.py]

<div class="font-large">

Given the [Computer Science Curriculum](https://cse.nd.edu/undergraduate/computer-science-curriculum-fall-2025-beyond/) (<i>[yld.me/mbfL](https://yld.me/mbfL)</i>):

1. How many `MATH` vs `PHYS` vs `CSE` courses?

2. How many sophomore `CSE` courses?

</div>

[cse-curriculum.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides12/cse-curriculum.py
