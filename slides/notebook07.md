---
title: "Notebook 07: Regular Expressions, Processes, Requests"
description: "Regular Expressions, Processes, Requests"
author: Peter Bui
keywords: notebook,sos,python,processes,requests,regular expressions
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/notebook07.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Regular Expressions<br>Processes, Requests

---

# Review: <strong class="gold">Unix Philosophy</strong>

<div class="slide-centered font-large">

Write programs that

<strong class="success">____________________________________________</strong>.

Write programs that

<strong class="success">____________________________________________</strong>.

Write programs that

<strong class="success">____________________________________________</strong>.

</div>

---

# Review: <strong class="gold">Data Structures</strong>

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

---

# Regular Expressions: <strong class="gold">Overview</strong>

<div class="columns">

<div class="centered">

A <strong class="success">regular expression</strong>

(*aka. <strong class="success">regex</strong>*) is a

<strong> ____________________________</strong>

that defines a search

<strong> ____________________________</strong>

that is used to **match** text.

</div>

<div class="centered">

<br>

<img src="static/img/slides07-regex-theory.svg">

</div>

</div>

---

<div class="font-small">

<table class="bordered">
<thead>
    <th class="info-bg">Metacharacter</th>
    <th class="info-bg">Description</th>
</thead>
<tbody>
    <tr class="success-bg"><td class="centered"><b>.</b></td><td>Match any single character</td></tr>
    <tr class="success-bg"><td class="centered"><b>[]</b></td><td>Match a single character contained in bracket</td></tr>
    <tr class="success-bg"><td class="centered"><b>[^]</b></td><td>Match a single character not contained in bracket</td></tr>
    <tr class="caution-bg"><td class="centered"><b>[a-z]</b></td><td>Match any lowercase letter</td></tr>
    <tr class="caution-bg"><td class="centered"><b>[0-9]</b></td><td>Match any numeric digit</td></tr>
    <tr class="warning-bg"><td class="centered"><b>*</b></td><td>Match preceding set zero or more times</td></tr>
    <tr class="warning-bg"><td class="centered"><b>?</b></td><td>Match preceding set zero or one time</td></tr>
    <tr class="warning-bg"><td class="centered"><b>+</b></td><td>Match preceding set one or more times</td></tr>
    <tr class="warning-bg"><td class="centered"><b>{m, n}</b></td><td>Match preceding set between m to n times</td></tr>
    <tr class="danger-bg"><td class="centered"><b>^</b></td><td>Match the starting position within a string</td></tr>
    <tr class="danger-bg"><td class="centered"><b>$</b></td><td>Match the ending position of a string</td></tr>
    <tr class="special-bg"><td class="centered"><b>()</b></td><td>Marks subexpression that can be recalled later</td></tr>
    <tr class="special-bg"><td class="centered"><b>\n</b></td><td>Match the nth marked subexpression matched</td></tr>
</tbody>
</table>

</div>

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

# Example: <strong class="gold">Web Scraping</strong>

> Write [Python] scripts that do the following:
>
>   - Extract the [HTML] title from a [URL].
>   - Extract the image sources from a [URL].
>   - Extract the [HTML] body from a [URL].

[Python]: https://python.org
[HTML]: https://en.wikipedia.org/wiki/HTML
[URL]: https://en.wikipedia.org/wiki/URL
