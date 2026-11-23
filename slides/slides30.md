---
title: "Slides 30: SQLite"
description: "SQLite"
author: Peter Bui
keywords: lecture,sos,databases,sqlite
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides30.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## SQLite

---

# SQLite: <span class="gold">Overview</span>

A <strong class="info">relational database</strong> is a collection of data
organized into <strong class="primary">tables</strong> that consist of <strong
class="special">rows</strong> of items that correspond to <strong
class="special">columns</strong>:

<div class="columns-1-2">

<div class="font-smaller">

<br>

- Has measures for <strong class="danger">data integrity</strong>.

- Allows for combining <strong class="warning">multiple datasets</strong>.

- Enables asking <strong class="info">detailed questions</strong>.

- Provides <strong class="success">scalable performance</strong>.

</div>

<div>

<a href="https://commons.wikimedia.org/wiki/File:SQLite370.svg" title="Part of the SQLite documentation, which has been released by author D. Richard Hipp to the public domain. SVG conversion by Mike Toews., Public domain, via Wikimedia Commons"><img width="600" height="284" src="https://thumb.wikimedia.org/wikipedia/commons/thumb/3/38/SQLite370.svg/960px-SQLite370.svg.png?utm_source=commons.wikimedia.org&amp;utm_campaign=index&amp;utm_content=thumbnail" srcset="https://thumb.wikimedia.org/wikipedia/commons/thumb/3/38/SQLite370.svg/330px-SQLite370.svg.png?utm_source=commons.wikimedia.org&amp;utm_campaign=index&amp;utm_content=thumbnail 330w, https://thumb.wikimedia.org/wikipedia/commons/thumb/3/38/SQLite370.svg/500px-SQLite370.svg.png?utm_source=commons.wikimedia.org&amp;utm_campaign=index&amp;utm_content=thumbnail 500w, https://thumb.wikimedia.org/wikipedia/commons/thumb/3/38/SQLite370.svg/960px-SQLite370.svg.png?utm_source=commons.wikimedia.org&amp;utm_campaign=index&amp;utm_content=thumbnail 960w, https://thumb.wikimedia.org/wikipedia/commons/thumb/3/38/SQLite370.svg/1280px-SQLite370.svg.png?utm_source=commons.wikimedia.org&amp;utm_campaign=index&amp;utm_content=thumbnail 1280w, https://thumb.wikimedia.org/wikipedia/commons/thumb/3/38/SQLite370.svg/3840px-SQLite370.svg.png?utm_source=commons.wikimedia.org&amp;utm_campaign=index&amp;utm_content=thumbnail 3840w" sizes="auto" loading="lazy" alt="SQLite370"></a>

<br>

<div class="alert info-bg centered">

[SQLite] is a lightweight and embeddable **relational database** implementation.

</div>

</div>

</div>

[SQLite]: https://www.sqlite.org/

---

# SQLite: <span class="gold">Structure</span>

<div class="columns">

<div>

- Every <strong class="info">database</strong> consists of <strong
  class="primary">tables</strong> that have a <strong
  class="caution">relationship</strong>.

- Each <strong class="primary">table</strong> consists of <strong
  class="special">rows</strong> and <strong class="special">columns</strong>.

- Each <strong class="special">column</strong> has a <strong
  class="warning">name</strong> and a <strong class="warning">type</strong>.

    - Duplicates?
    - Empty?
    - Default?

- Each <strong class="special">row</strong> is the actual <strong
  class="info">data</strong>.

</div>

<div class="middled">

<table class="bordered centered">
<thead>
    <th class="special-bg">id</th>
    <th class="special-bg">room</th>
    <th class="special-bg">message</th>
</thead>
<tbody>
<tr class="info-bg"><td>0</td><td>dillon-210</td><td>Sup bro</td></tr>
<tr class="caution-bg"><td>1</td><td>dillon-210</td><td>Hey bro</td></tr>
<tr class="info-bg"><td>2</td><td>welsh-204</td><td>Yo girl</td></tr>
<tr class="caution-bg"><td>3</td><td>welsh-204</td><td>Hi girl</td></tr>
</tbody>
</table>

</div>

</div>

---

# SQLite: <span class="gold">Interfaces</span>

We can interact with a [SQLite] <strong class="info">database</strong> via the
<strong class="success">command line interface</strong>:

```bash
# Interact with doornote.db sqlite database
$ sqlite3 doornote.db
SQLite version 3.46.1 2024-08-13 09:16:08
Enter ".help" for usage hints.
sqlite> .tables
Messages
```

<br>

<div class="alert info-bg centered">

We can interact with a [SQLite] <strong class="info">database</strong><br>via a
<strong class="warning">graphical interface</strong> such as [SQLite Browser].

</div>

[SQLite Browser]: https://sqlitebrowser.org/

---

<!-- _class: lead -->

# SQL

---

# SQL: <span class="gold">Overview</span>

To programmatically interact with a [SQLite] <strong
class="info">database</strong>, we use <strong class="warning">SQL</strong> (<i
class="muted">Structured Query Language</i>):

<table class="bordered">
<thead>
    <th class="special-bg">Verb</th>
    <th class="special-bg">Description</th>
</thead>
<tbody>
<tr class="success-bg">
    <td><b>CREATE</b></td>
    <td>Create a <strong class="primary">table</strong> and specify its <strong
    class="special">columns</strong>.</td>
</tr>
<tr class="danger-bg">
    <td><b>DROP</b></td>
    <td>Remove a <strong class="primary">table</strong>.</td>
</tr>
<tr class="success-bg">
    <td><b>INSERT</b></td>
    <td>Add <strong class="special">row(s)</strong> to a <strong
    class="primary">table</strong>.</td>
</tr>
<tr class="caution-bg">
    <td><b>UPDATE</b></td>
    <td>Update <strong class="special">row(s)</strong> in a  <strong
    class="primary">table</strong>.</td>
</tr>
<tr class="danger-bg">
    <td><b>DELETE</b></td>
    <td>Remove <strong class="special">row(s)</strong> from a  <strong
    class="primary">table</strong>.</td>
</tr>
<tr class="info-bg">
    <td><b>SELECT</b></td>
    <td>Get <strong class="special">row(s)</strong> from a  <strong
    class="primary">table</strong>.</td>
</tr>
</tbody>
</table>

---

# SQL: <span class="gold">CRUD</span>

Many <strong class="info">database</strong> and <strong class="special">web
applications</strong> are classified as [CRUD] applications:

<br>

<table class="bordered centered">
<thead>
    <th class="special-bg">Operation</th>
    <th class="special-bg">SQL</th>
    <th class="special-bg">HTTP</th>
</thead>
<tbody>
<tr class="success-bg">
    <td><b>Create</b></td>
    <td><b>INSERT</b></td>
    <td><b>PUT / POST</b></td>
</tr>
<tr class="info-bg">
    <td><b>Read</b></td>
    <td><b>SELECT</b></td>
    <td><b>GET</b></td>
</tr>
<tr class="warning-bg">
    <td><b>Update</b></td>
    <td><b>UPDATE</b></td>
    <td><b>PUT / POST</b></td>
</tr>
<tr class="danger-bg">
    <td><b>Delete</b></td>
    <td><b>DELETE</b></td>
    <td><b>DELETE</b></td>
</tr>
</tbody>
</table>

[CRUD]: https://en.wikipedia.org/wiki/Create,_read,_update_and_delete

---

# SQL: <span class="gold">CREATE and DROP</span>

To create a <strong class="primary">table</strong> and specify its <strong
class="special">column</strong> types, we use the <strong
class="success">CREATE</strong> command:

```sql
CREATE TABLE IF NOT EXISTS Messages(
    id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    room        VARCHAR(20) NOT NULL,
    message     VARCHAR(500) NOT NULL
);
```

Conversely, to remove a table, we use the <strong class="danger">DROP</strong>
command:

```sql
DROP TABLE Messages;
```

---

# SQL: <span class="gold">INSERT / UPDATE / DELETE</span>

To add a <strong class="special">row</strong> of data to the <strong
class="info">database</strong>, we use the <strong
class="success">INSERT</strong> command:

```sql
INSERT INTO Messages (room, message) VALUES ("dillon-210", "sup bro");
```

Additionally, to modify a <strong class="special">row</strong> of data, we use
the <strong class="caution">UPDATE</strong> command:

```sql
UPDATE Messages SET room="dillon-163" WHERE id=1;
```

Finally, to remove a <strong class="special">row</strong> of data, we use
the <strong class="danger">DELETE</strong> command:

```sql
DELETE FROM Messages WHERE room="dillon-210";
```


---

# SQL: <span class="gold">SELECT</span>

To fetch <strong class="special">rows</strong> from a <strong
class="info">database</strong>, we can use the <strong
class="info">SELECT</strong> command:

```sql
-- Retrieve all rows with every column
SELECT * FROM Messages;

-- Retrieve messages from all rows
SELECT message from MESSAGES;

-- Retrieve messages from rows that match criteria
SELECT message from MESSAGES WHERE room="dillon-210";
```

---

<!-- _class: lead -->

# Python + SQLite

---

# Python + SQLite: <span class="gold">Connections</span>

To utilize [SQLite] with <strong class="success">Python</strong>, we use the
[sqlite3] module to establish connections to a <strong
class="info">database</strong>:

```python
import sqlite3                          # Import module

conn = sqlite3.connect('doornote.db')   # Open connection to database

conn.commit()                           # Save changes

conn.close()                            # Close database connection
```

[sqlite3]: https://docs.python.org/3/library/sqlite3.html

---

# Python + SQLite: <span class="gold">Cursors</span>

To perform <strong class="warning">SQL</strong> operations, we first create a
<strong class="caution">cursor</strong> and then use it to execute <strong
class="warning">SQL</strong> statements:

```python
# Create cursor and define SQL statement
cursor    = conn.cursor()
statement = 'SELECT * FROM Messages'

# Execute SQL statement and print each resulting row
cursor.execute(statement)
for row in cursor.fetchall():
    print(row)
```

---

# Python + SQLite: <span class="gold">Statements</span>

Rather than manually interpolating <strong class="warning">SQL</strong>
statements, we can use the `execute` method to prepare <strong
class="warning">SQL</strong> values for us:

```python
# Create cursor and define SQL statement
cursor    = conn.cursor()
statement = 'INSERT INTO Messages (room, message) VALUES (?, ?)'

# Execute prepared SQL statement
cursor.execute(statement, ("dillon-210", "sup bro"))
```

<br>

<div class="alert danger-bg centered font-smaller">

Using **prepared** <strong class="warning">SQL</strong> statements<br>is one way
to avoid [SQL injections]!

</div>

[SQL injections]: https://en.wikipedia.org/wiki/SQL_injection

---

# Python + SQLite: <span class="gold">Transactions</span>

In order to record changes to the <strong class="info">database</strong>, we
have to call the `commit` method on the <strong class="info">database</strong>
connection.  To have this happen automatically, we can use the `with`
statement:

```python
with conn:
    statement = 'SELECT message FROM Messages WHERE room=?'
    cursor    = conn.cursor()
    cursor.execute(statement, ("dillon-210",))
	for row in cursor.fetchall()
		print(row)
```

<br>

<div class="alert info-bg centered font-smaller">

Using the `with` statement causes the **database** operations to occur as a single
**transaction** (*ie. everything happens or nothing happens*).

</div>

---

# Python + SQLite: [doornote.py]

> Use [sqlite3] in [doornote.py], which is a <strong class="special">web
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

[doornote.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides30/doornote.py
