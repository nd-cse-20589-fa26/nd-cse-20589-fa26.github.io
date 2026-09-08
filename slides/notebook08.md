---
title: "Notebook 08: Processes, Requests, JSON"
description: "Processes, Requests, JSON"
author: Peter Bui
keywords: notebook,sos,python,processes,requests,csv
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/notebook07.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Processes, Requests, JSON

---

# Regular Expressions: <span class="gold">Pokemon</span>

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

# Process: <strong class="gold">Life Cycle</strong>

<div class="columns-1-3">

<div class="slide-centered margin-top-0-5">

A <strong class="success">process</strong> is a

<strong> ________________________</strong>

<strong> _______________________</strong>;

it is a unit of

<strong> _______________________</strong>.

</div>

<div class="slide-centered margin-top-0-5">

<img src="static/img/notebook08-process-life-cycle-blank.svg" width="675">

</div>

</div>

---

# Requests: <strong class="gold">Web Scraping</strong>

> Write [Python] code that does the following:
>
>   - Extract the [HTML] title from a [URL].
>   - Extract the image sources from a [URL].
>   - Extract the [HTML] body from a [URL].

[Python]: https://python.org
[HTML]: https://en.wikipedia.org/wiki/HTML
[URL]: https://en.wikipedia.org/wiki/URL

---

# JSON: <strong class="gold">Wikipedia</strong>

> Write a script that lists all the [Wikipedia] entries for a particular search
> term:

```bash
$ ./wikipedia.py python
   1.   Python
        Look up Python or python in Wiktionary, the free dictionary. Python may 
        refer to: Pythonidae, a family of nonvenomous snakes found in Africa,
        Asia, and 

   2.   Python (codename)
        Python was a Cold War contingency plan of the British Government for 
        the continuity of government in the event of nuclear war. Following the 
        report of
...
```

[Wikipedia]: https://www.wikipedia.org/
[wikipedia.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides09/wikipedia.py 
