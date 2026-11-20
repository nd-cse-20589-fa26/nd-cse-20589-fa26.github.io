---
title: "Slides 29: Databases"
description: "Databases"
author: Peter Bui
keywords: lecture,sos,databases
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides29.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Databases

---

# Databases: <span class="gold">Overview</span>

Most <strong class="success">software systems</strong>, including <strong
class="special">web applications</strong>, usually store information in a
<strong class="info">database</strong>, which is an organized collection of
data that can be easily **accessed**, **managed**, **updated**, and
**queried**.

<div class="columns">

<div class="font-smaller">

- For simple data, it is sufficient to use a <strong class="danger">flat
  file</strong> to store data.

- For structured data, it is possible to use <strong
  class="warning">CSV</strong> or <strong class="warning">JSON</strong>
  formatted files.

- For large amounts of data, however, it is necessary to use a <strong
  class="success">database management system</strong> (*DBMS*) such as
  [SQLite].

</div>

<div>

<img src="static/img/software-systems.svg">

</div>

</div>

[SQLite]: https://www.sqlite.org/

---

# Databases: [doornote.py]

> Add a database to [doornote.py], which is a <strong class="special">web
> application</strong> that allows users to list the `messages` left by others
> for a particular `room` or allows users to post a `message` to a particular
> `room`.

```bash
# Start doornote web application
$ ./doornote.py 0.0.0.0 9999

# Get messages for Dillon 210
$ curl localhost:9999/room/dillon-210

# Post message to Dillon 210
$ curl -d 'Hello' localhost:9999/room/dillon-210
```

[doornote.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides29/doornote.py

---

# Databases: <span class="gold">Version 0</span>

<div class="columns">

<div>

Since we need to store `messages` for each `room`, we can create a <strong
class="primary">dict</strong> where each `room` maps to a <strong
class="primary">list</strong> of `messages`.

<br>

<div class="alert danger-bg centered">

This is **fast** and **simple** but offers no <strong
class="info">persistence</strong>.  If server **crashes** or **exits**, then
all data is lost!

</div>

</div>

<div>

```python
class Database0:
    ''' Database 0: Only stored in memory '''

    def __init__(self):
        self.rooms = {}

    def messages(self, room: str) -> list[str]:
        ''' Return messages associated with room. '''
        return self.rooms.get(room, [])

    def append(self, room: str, message: str):
        ''' Add message to end of list associated with room. '''
        try:
            self.rooms[room].append(message)
        except KeyError:
            self.rooms[room] = [message]

    def count(self, room: str) -> int:
        ''' Return number of messages for room. '''
        return len(self.rooms.get(room, []))
```


</div>

</div>

---

# Databases: <span class="gold">Version 1</span>

<div class="columns">

<div>

To add <strong class="info">persistence</strong>, we can consider storing the `messages` of each
`room` in a separate <strong class="warning">file</strong>.

<br>

<div class="alert warning-bg centered">

This is **simple** but is slow: need to `open` and perform
<strong class="caution">I/O</strong> for every operation.  Moreover, with many `rooms`, we
would end up with a lot of <strong class="warning">files</strong>.

</div>

</div>

<div>

```python
class Database1:
    ''' Database 1: Stored in multiple files (one per room) '''

    def __init__(self, prefix='doornote'):
        self.prefix = prefix

    def messages(self, room: str) -> list[str]:
        ''' Return messages associated with room. '''
        path = f'{self.prefix}.{room}'
        try:
            with open(path) as stream:
                return [line.strip() for line in stream]
        except OSError:
            return []

    def append(self, room: str, message: str):
        ''' Add message to end of list associated with room. '''
        path = f'{self.prefix}.{room}'
        with open(path, 'a') as stream:
            stream.write(f'{message}\n')

    def count(self, room: str) -> int:
        ''' Return number of messages for room. '''
        path = f'{self.prefix}.{room}'
        with open(path) as stream:
            return sum(1 for _ in stream)
```

</div>

</div>

---

# Databases: <span class="gold">Version 2</span>

<div class="columns">

<div>

Rather than use many <strong class="warning">files</strong>, we can use a
single structured <strong class="warning">JSON file</strong>.

<br>

<div class="alert caution-bg centered">

This is **simple** and a bit more efficient because we only need perform
<strong class="caution">I/O</strong> when initially **loading** the <strong
class="info">database</strong> and when **saving** after an `append`.

</div>

</div>

<div>

```python
class Database2:
    ''' Database 2: Stored in a single JSON file '''

    def __init__(self, path='doornote.json'):
        self.path = path
        self.load()

    def load(self):
        try:
            with open(self.path) as stream:
                self.rooms = json.load(stream)
        except OSError:
            self.rooms = {}
    def save(self):
        with open(self.path, 'w') as stream:
            json.dump(self.rooms, stream)

    def messages(self, room: str) -> list[str]:
        ''' Return messages associated with room. '''
        return self.rooms.get(room, [])

    def append(self, room: str, message: str):
        ''' Add message to end of list associated with room. '''
        try:
            self.rooms[room].append(message)
        except KeyError:
            self.rooms[room] = [message]

        self.save()

    def count(self, room: str) -> int:
        ''' Return number of messages for room. '''
        return len(self.rooms.get(room, []))
```

</div>

</div>

---

# Databases: <span class="gold">Memory Hierarchy</span>

<div class="centered">

<br>

<a href="https://gist.github.com/hellerbarde/2843375">
<img src="https://camo.githubusercontent.com/21e9781dff39ae0055959d1c686278591144f412c759dc77ebe1843e25376024/687474703a2f2f692e696d6775722e636f6d2f6b307431652e706e67" class="framed">
</a>

</div>

---

# Databases: <span class="gold">Reflection</span>

While using <strong class="danger">flat files</strong> or even structured
<strong class="warning">JSON files</strong> works for simple applications, they
are **insufficient** for larger and more complex systems.

- Changing data often requires <strong class="caution">loading the entire file
  into memory</strong>, making the change, and then writing the data back out
  to disk.

- <strong class="success">Querying</strong> or <strong
  class="success">searching</strong> data often requires a full search of all
  data.

<br>

<div class="alert info-bg centered">

For **fast** and **persistent** data storage, we will want to use a **database
management system** such as [SQLite].

</div>
