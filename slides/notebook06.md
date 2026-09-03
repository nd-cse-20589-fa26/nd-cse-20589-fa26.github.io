---
title: "Notebook 06: Data Structures, Arguments, I/O"
description: "Data Structures, Arguments, I/O"
author: Peter Bui
keywords: notebook,sos,python,data structures,arguments,i/o
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/notebook06.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Data Structures, Arguments,<br>I/O, Processes

---

# Tour of Python: <strong class="gold">Scripting</strong>

<div class="font-large">

1. <strong class="caution">Data Structures</strong>

2. <strong class="warning">Arguments</strong>

3. <strong class="danger">I/O</strong>

4. <strong class="success">Processes</strong>

</div>

---

# Example: [Anagrams](https://github.com/nd-cse-20589-fa26/examples/blob/master/slides05/anagram.py)

> Given two words, determine if they are [anagrams].

```bash
$ ./anagram.py -i       # Ignore case
listen silent
ANAGRAM!
army Mary
ANAGRAM!
card dare
NOT ANAGRAM!
```

[anagrams]: https://en.wikipedia.org/wiki/Anagram

---

# Example: [randomsay.py]

> Write a <strong class="success">Python</strong> script that chooses a random
<strong class="caution">cow</strong> from [cowsay] and then runs the command
with the chosen <strong class="caution">cow</strong>.

```bash
$ ./randomsay.py hello, world
 ______________
< hello, world >
 --------------
        \  ^___^
         \ (ooo)\_______
           (___)\       )\/\
                ||----w |
                ||     ||
```

[cowsay]: https://github.com/cowsay-org/cowsay
[randomsay.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides06/randomsay.py

---

# Example: [leetspeak.py]

> Write a [leetspeak] translator.

```bash
# Run with default mapping
$ echo we are the tide | ./leetspeak.py
w3 4r3 th3 t1d3

# Run with custom mapping
$ echo we are the tide | ./leetspeak.py -f et -t 37
w3 ar3 7h3 7id3
```

[leetspeak.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides05/leetspeak.py
[leetspeak]: https://en.wikipedia.org/wiki/Leet

---

# Data Structures: <span class="gold">Summary</span>

<div class="slide-centered">

<table class="bordered">
<thead>
    <th>Container</th>
    <th>C</th>
    <th>Python</th>
    <th>Python Syntax</th>
</thead>
<tbody>
    <tr class="success-bg" height="100px">
        <td class="centered" width="300px" height="100px">&nbsp;<br>&nbsp;</td>
        <td class="centered" width="300px"></td>
        <td class="centered" width="300px"></td>
        <td class="centered" width="300px"></td>
    </tr>
    <tr class="caution-bg" height="100px">
        <td class="centered" width="300px" height="100px">&nbsp;<br>&nbsp;</td>
        <td class="centered"></td>
        <td class="centered"></td>
        <td class="centered"></td>
    </tr>
    <tr class="warning-bg" height="100px">
        <td class="centered" width="300px" height="100px">&nbsp;<br>&nbsp;</td>
        <td class="centered"></td>
        <td class="centered"></td>
        <td class="centered"></td>
    </tr>
    <tr class="danger-bg" height="100px">
        <td class="centered" width="300px" height="100px">&nbsp;<br>&nbsp;</td>
        <td class="centered"></td>
        <td class="centered"></td>
        <td class="centered"></td>
    </tr>
</tbody>
</table>

</div>
