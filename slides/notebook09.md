---
title: "Notebook 09: Requests, CSV, JSON"
description: "Requests, CSV, JSON"
author: Peter Bui
keywords: notebook,sos,python,requests,csv,json
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/notebook09.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Requests, CSV, JSON

---

# Requests: <strong class="gold">HTTP</strong>

<div class="slide-centered">

<img src="static/img/slides02-ssh-model-blank.svg">

</div>

---

# Requests: <strong class="gold">Web Scraping</strong>

> Write [Python] code that does the following:
>
>   - Extract the [HTML] title from a [URL].
>   - Extract the image sources from a [URL].

[Python]: https://python.org
[HTML]: https://en.wikipedia.org/wiki/HTML
[URL]: https://en.wikipedia.org/wiki/URL

---

# CSV: <strong class="gold">Professors</strong>

> Write a script that parses the [CSV] data at
> [https://yld.me/raw/bA7.csv](https://yld.me/raw/bA7.csv) and then lists the
> professors' netid and phone numbers.

```bash
$ ./professors.py
     jbb 574-631-8810
 skumar5 574-631-7381
    pbui 574-631-1467
...
adingler 574-631-8752
   tjung 574-631-8322
wtheisen 419-905-6474
```

[CSV]: https://docs.python.org/3/library/csv.html

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
