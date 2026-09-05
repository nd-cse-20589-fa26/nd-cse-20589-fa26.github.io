---
title: "Slides 09: JSON"
description: "JSON"
author: Peter Bui
keywords: lecture,sos,python,json
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides09.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## JSON

---

# JSON: <span class="gold">Overview</span>

A common way to represent structured data is [JSON] (*JavaScript Object
Notation*).

In this format, objects such as <strong class="primary">strings</strong>,
<strong class="primary">lists</strong>, and <strong
class="primary">dictionaries</strong> share the same syntax as <strong
class="success">Python</strong>:

```json
{
    "numbers": [1, 2, 3]
}
```

That is, [JSON] is a way to represent <strong class="warning">data structures</strong> in
textual format for easy communication.

[JSON]: https://www.json.org/

---

# JSON: <span class="gold">Loading</span>

To parse a [JSON] string into <strong class="success">Python</strong> object,
you can use the [json.loads] function:

```python
# Load json module
>>> import json

# Parse JSON string into Python object
>>> data = json.loads('{"numbers": [1, 2, 3]}')
>>> data['numbers']
[1, 2, 3]
```

This will convert the string containing [JSON] data into the corresponding
Python <strong class="warning">data structures</strong>.

[json.loads]: https://docs.python.org/3/library/json.html#json.loads

---

# JSON: <span class="gold">Dumping</span>

To convert a <strong class="success">Python</strong> object into a [JSON]
string, you can use the [json.dumps] function:

```python
# Convert data dictionary into JSON string
>>> data = {'numbers': [1, 2, 3]}
>>> print(json.dumps(data, indent=2))
{
  "numbers": [
    1,
    2,
    3
  ]
}
```

[json.dumps]: https://docs.python.org/3/library/json.html#json.dumps

---

# JSON: <span class="gold">Requests</span>

To fetch [JSON] data via [HTTP], we can use the [requests] package:

```python
# Download Reading 03 Quiz JSON Data
url = 'https://pnutz.h4x0r.space/courses/cse.20589.fa26/static/json/reading03.json'
response = requests.get(url)
quiz = response.json()  # Convert JSON text into Python objects

# Iterate over quiz questions and print their type
for question in quiz:
    print(question, quiz[question]['type'])
```

[HTTP]: https://en.wikipedia.org/wiki/HTTP
[requests]: https://requests.readthedocs.io/

---

# Example: [wikipedia.py]

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
