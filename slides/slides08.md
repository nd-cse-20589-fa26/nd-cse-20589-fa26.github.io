---
title: "Slides 08: CSV"
description: "CSV"
author: Peter Bui
keywords: lecture,sos,python,csv
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides08.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## CSV

---

# CSV: <span class="gold">Overview</span>

In [CSV] formatted data, fields are separated by a **delimiter** such as a
**comma**:

```
field1,field2,field3
```

One way to process this data is by using [str.split] on each row:

```python
with open('data.csv') as stream:
    for row in stream:
        fields = line.split(',')
        print(fields[0])
```

[CSV]: https://en.wikipedia.org/wiki/Comma-separated_values
[str.split]: https://docs.python.org/3/library/stdtypes.html#str.split

---

# CSV: [csv.reader]

Alternatively, a more robust way to process [CSV] data is using the
[csv](https://docs.python.org/3/library/csv.html) module:

```python
# Print all the users in /etc/passwd and their shells
with open('/etc/passwd') as stream:
    for fields in csv.reader(stream, delimiter=':'):
        print(fields[0], fields[-1])
```

This will parse the [CSV] data such that each row of fields is represented by a
<strong class="primary">list</strong>.  This is more robust than [str.split] as
it will handle spaces or quotes for you.

[csv.reader]: https://docs.python.org/3/library/csv.html#csv.reader

---

# CSV: [csv.DictReader]

If the [CSV] data has a header, then you can use the [csv.DictReader] to
generate a <strong class="primary">dict</strong> for each row instead of a
<strong class="primary">list</strong>:

```python
# Download CSV data and then print netid and phone number of each professor
response = requests.get('https://yld.me/raw/bA7.csv')
for professor in csv.DictReader(response.text.splitlines()):
    print(professor['netid'], professor['phone'])
```

With this function, each row of fields is represented by a <strong
class="primary">dict</strong> where the column name corresponds to the **field
in the first header row**.

[csv.DictReader]: https://docs.python.org/3/library/csv.html#csv.DictReader

---

# CSV: [pgrep.py]

> Write a version of [pgrep] which searches all the processes on a system and
> prints their PID if they match the <strong class="success">regular
> expression</strong>.

```bash
# Search for all bash processes that belong to pbui
$ ./pgrep.py -u pbui -a bash
...
22319 -bash
30428 -bash
31257 -bash
330545 -bash
```

[pgrep]: https://man7.org/linux/man-pages/man1/pgrep.1.html
[pgrep.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides08/pgrep.py

