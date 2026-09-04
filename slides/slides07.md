---
title: "Slides 07: Regular Expressions"
description: "Regular Expressions"
author: Peter Bui
keywords: lecture,sos,python,regular expressions
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides07.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Regular Expressions

---

# Regular Expressions: <span class="gold">Overview</span>

A <strong class="success">regular expression</strong> (*aka. <strong
class="success">regex</strong>*) is a sequence of characters that define a
search **pattern** that is used to match text.

```bash
# Match password entries with the pattern "user:"
$ grep -i ' user:' /etc/passwd
$ grep -E ' (user|User):' /etc/passwd
$ grep -E ' [uU]ser:' /etc/passwd
```

- Based on <strong class="danger">formal language theory</strong>.

- Many different implementations and syntaxes (*varies between tools*).

---

# Regular Expressions: <span class="gold">Theory</span>

<div class="columns-1-2">

<div class="centered">

A <strong class="success">regular expression</strong> is a specification of a
regular language that can represented by a <strong class="special">finite
automaton (FA)</strong>.

</div>

<div class="centered margin-top-0-5">

<img src="static/img/slides07-regex-theory.svg">

</div>

</div>

```bash
# Match numbers that start with 2 and end with 8
$ grep -E '2[0-9]*8' /etc/passwd
```

---

# Regex: <span class="gold">Syntax</span> (<i class="muted">Sets</i>)

<table class="bordered">
<thead>
    <th class="info-bg">Metacharacter</th>
    <th class="info-bg">Description</th>
</thead>
<tbody class="font-smaller">
    <tr><td class="centered"><b>.</b></td><td>Match any single character</td></tr>
    <tr><td class="centered"><b>[]</b></td><td>Match a single character contained in bracket</td></tr>
    <tr><td class="centered"><b>[^]</b></td><td>Match a single character not contained in bracket</td></tr>
</tbody>
</table>

```bash
# Match five letter string that starts and ends with a colon
$ grep -Eo ':...:' /etc/passwd

# Match five letter string that starts and ends with a colon but only contains letters
$ grep -Eo ':[a-z][a-z][a-z]:' /etc/passwd

# Match five letter string that starts and ends with a colon but not any colons
$ grep -Eo ':[^:][^:][^:]:' /etc/passwd
```

---

# Regex: <span class="gold">Syntax</span> (<i class="muted">Predefined Sets</i>)

<table class="bordered">
<thead>
    <th class="info-bg">Classes</th>
    <th class="info-bg">Description</th>
</thead>
<tbody class="font-smaller">
    <tr><td class="centered"><b>[a-z]</b></td><td>Match any lowercase letter</td></tr>
    <tr><td class="centered"><b>[A-Z]</b></td><td>Match any uppercase letter</td></tr>
    <tr><td class="centered"><b>[0-9]</b></td><td>Match any numeric digit</td></tr>
    <tr><td class="centered"><b>\d</b></td><td>Match any numeric digit</td></tr>
    <tr><td class="centered"><b>\D</b></td><td>Match any non-digit</td></tr>
    <tr><td class="centered"><b>\w</b></td><td>Match any word character (<i>letters, numbers, underscores</i>)</td></tr>
    <tr><td class="centered"><b>\W</b></td><td>Match any non-word character (<i>spaces, punctuation</i>)</td></tr>
    <tr><td class="centered"><b>\s</b></td><td>Match any space character (<i>spaces, tabs, newlines</i>)</td></tr>
    <tr><td class="centered"><b>\S</b></td><td>Match any non-space character</td></tr>
</tbody>
</table>

---

# Regex: <span class="gold">Syntax</span> (<i class="muted">Quantifiers</i>)

<table class="bordered">
<thead>
    <th class="info-bg">Metacharacter</th>
    <th class="info-bg">Description</th>
</thead>
<tbody class="font-smaller">
    <tr><td class="centered"><b>*</b></td><td>Match preceding set zero or more times</td></tr>
    <tr><td class="centered"><b>?</b></td><td>Match preceding set zero or one time</td></tr>
    <tr><td class="centered"><b>+</b></td><td>Match preceding set one or more times</td></tr>
    <tr><td class="centered"><b>{m, n}</b></td><td>Match preceding set between m to n times</td></tr>
</tbody>
</table>

```bash
# Match five letter string that starts and ends with a colon but only contains letters
$ grep -Eo ':[a-z]{3}:' /etc/passwd

# Match string that starts and ends with a /
$ grep -Eo '/.*/' /etc/passwd

# Match string of numbers with only odd digits
$ grep -Eo '[13579]+' /etc/passwd
```

---

# Regex: <span class="gold">Syntax</span> (<i class="muted">Anchors</i>)

<table class="bordered">
<thead>
    <th class="info-bg">Metacharacter</th>
    <th class="info-bg">Description</th>
</thead>
<tbody class="font-smaller">
    <tr><td class="centered"><b>^</b></td><td>Match the starting position within a string</td></tr>
    <tr><td class="centered"><b>$</b></td><td>Match the ending position of a string</td></tr>
</tbody>
</table>

```bash
# Match all lines that begin with _
$ grep -Eo '^_.*' /etc/passwd

# Match all lines that end with nolgin
$ grep -Eo '.*nologin$' /etc/passwd
```

---

# Regex: <span class="gold">Syntax</span> (<i class="muted">Grouping</i>)

<table class="bordered">
<thead>
    <th class="info-bg">Metacharacter</th>
    <th class="info-bg">Description</th>
</thead>
<tbody class="font-smaller">
    <tr><td class="centered"><b>()</b></td><td>Marks subexpression that can be recalled later</td></tr>
    <tr><td class="centered"><b>\n</b></td><td>Match the nth marked subexpression matched</td></tr>
    <tr><td class="centered"><b>|</b></td><td>Match either expression</td></tr>
</tbody>
</table>

```bash
# Match all numbers that begin and end with the same digit
$ grep -Eo '([0-9])[0-9]*\1' /etc/passwd

# Match strings that with var or usr
$ grep -Eo '/(var|usr).*/' /etc/passwd
```

---

# Example: <span class="gold">Pokemon</span>

<div class="columns-1-4">

<div>

**Given**:

pikachu
bulbasaur
charmander
chespin
squirtle
meowth
togepi
oshawott
abra
jigglypuff

</div>

<div>

> Write a <strong class="success">regex</strong> to match:

<img src="https://platform.theverge.com/wp-content/uploads/sites/2/chorus/uploads/chorus_asset/file/6839749/pokemon.0.png" class="float-right framed margin-top-0-5" width="240px">

<div class="font-smaller">

1. **All** the strings

2. Only **charmander** and **chespin**

3. All the words with **two t's**

4. Words that **don't start with a vowel**

5. All words with **two consecutive vowels**

6. All words with **two consecutive letters (same)**

7. All words that **begin** and **end with the same letter**

8. All words with **exactly 2 of r, s, or t**

</div>

</div>

</div>

---

# Regular Expressions: [re.search]

To use <strong class="success">regular expressions</strong> in <strong
class="success">Python</strong>, load the [re] module and then use the
[re.search] function to see if a pattern can be found in a string:

```python
# Load regular expressions module
>>> import re

# Search 'cse.20589.sp26' for first numeric sequence
>>> if matched := re.search(r'[0-9]+', 'cse.20589.sp26'): print(matched)
<re.Match object; span=(4, 9), match='20589'>

# Print first match
>>> matched[0]
```

[re]: https://docs.python.org/3/library/re.html
[re.search]: https://docs.python.org/3/library/re.html#re.search

---

# Example: [html_title.py]

> Write a program that extracts and prints the [HTML] title from a [URL].

```bash
# Extract and print title of CSE Home Page
$ ./html_title.py https://cse.nd.edu
Home - Computer Science and Engineering
```

[html]: https://en.wikipedia.org/wiki/HTML
[url]: https://en.wikipedia.org/wiki/URL
[html_title.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides07/html_title.py

---

# Regular Expressions: [re.findall]

To search for all the matches in a string, use [re.findall] on a pattern to get
a <strong class="primary">list</strong> of all the found matches.

```python
# Search 'cse.20589.sp26' for all numeric sequences
>>> for matched in re.findall(r'[0-9]+', 'cse.20589.sp26'): print(matched)
20589
26

# Search /etc/passwd for all usernames that have a nologin shell
>>> regex = re.compile(r'^([^:]+):.*:.*nologin$')   # Compiling is optional
>>> text  = open('/etc/passwd').read()              # Search all lines
>>> for matched in re.findall(rx, text, flags=re.MULTILINE): print(matched)
daemon
...
_chrony
```

[re.findall]: https://docs.python.org/3/library/re.html#re.findall

---

# Example: [html_images.py]

> Write a program that extracts and prints all the [HTML] images from a [URL].

```bash
# Extract and print image sources on course website
$ ./html_images.py https://pnutz.h4x0r.space/courses/cse.20589.fa26
static/img/software-systems.svg
static/img/office-hours.svg
```

[html_images.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides07/html_images.py

---

# Regular Expressions: [re.sub]

In addition to [grep], another common [Unix] tool that utilizes <strong
class="success">regular expressions</strong> is [sed]:

```bash
$ echo 'blue and gold' | sed 's/gold/green/'
blue and green
```

As can been seen, [sed] is useful for searching and replacing text.  In <strong
class="success">Python</strong>, this can be replicated using [re.sub]:

```python
>>> re.sub(r'gold', 'green', 'blue and gold')
'blue and green'
```

[Unix]: https://en.wikipedia.org/wiki/Unix
[grep]: https://man7.org/linux/man-pages/man1/grep.1.html
[sed]: https://man7.org/linux/man-pages/man1/sed.1.html
[re.sub]: https://docs.python.org/3/library/re.html#re.sub

---

# Example: [html_body.py]

> Write a program that extracts and prints the [HTML] body from a [URL] without
> any [HTML] tags.

```bash
# Extract and print body from example.com without HTML tags
$ ./html_body.py https://example.com
Example Domain  This domain is for use in documentation examples without
needing permission. Avoid use in operations.   Learn more
```

[html_body.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides07/html_body.py
