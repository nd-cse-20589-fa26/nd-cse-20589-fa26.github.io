---
title: "Notebook 03: Files, Processes, I/O"
description: "Files, Processes, I/O"
author: Peter Bui
keywords: notebook,sos,files,processes,io
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/notebook03.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Files, Processes, I/O

---

# Files: <strong class="gold">Motivating Questions</strong>

<div class="font-large">

1. Where is <strong class="primary">ls</strong> located?

2. How large is my <strong class="caution">~/.bashrc</strong>?

3. How do I <strong class="danger">prevent</strong> people from reading my files?

4. Where did I put that <strong class="warning">.c</strong> file?

</div>

---

# Files: <strong class="gold">File System</strong>

<div class="columns">

<div>

<div class="centered">

<br>

<div class="alert warning-bg">

Where is <strong class="primary">ls</strong> located?

</div>

<br>

The unix <strong class="primary">file system</strong> is

structured as a

<strong class="success">____________________</strong>

([man 7 hier]).

</div>

[man 7 hier]:   https://man7.org/linux/man-pages/man7/hier.7.html
[inode]:        https://man7.org/linux/man-pages/man7/inode.7.html


</div>

<div>

<br>

<img src="static/img/slides03-files-hierarchy-blank.png">

</div>

</div>

---

# Files: <strong class="gold">Metadata</strong>

<div class="columns-1-2">

<div class="centered">

<br>

<div class="alert warning-bg">

How large is my <strong class="caution">~/.bashrc</strong>?

</div>

<br>

Every <strong class="success">file system object</strong> is represented by a
<strong class="danger">data structure</strong> called an

<strong class="caution">____________________</strong>.

</div>

<div>

<div class="centered">

<br>

<img src="static/img/slides03-files-inode-blank.png">

</div>

</div>

</div>

---

# Files: <strong class="gold">Permissions</strong>

<div class="centered">

<br>

<div class="alert warning-bg">

How do I <strong class="danger">prevent</strong> people from reading my work?

</div>

</div>

<table class="bordered">
<thead>
    <th>Owner</th>
    <th>Group</th>
    <th>World</th>
    <th>Octal</th>
</thead>
<tbody>
<tr class="caution-bg font-large">
    <td class="centered" width="200">r w x</td>
    <td class="centered" width="200">r w x</td>
    <td class="centered" width="200">r w x</td>
    <td class="centered" width="200"></td>
</tr>
<tr class="success-bg font-large">
    <td class="centered" width="200"></td>
    <td class="centered" width="200"></td>
    <td class="centered" width="200"></td>
    <td class="centered" width="200">&nbsp;</td>
</tr>
<tr class="info-bg font-large">
    <td class="centered" width="200"></td>
    <td class="centered" width="200"></td>
    <td class="centered" width="200"></td>
    <td class="centered" width="200">755</td>
</tr>
</tbody>
</table>

---

# Processes: <strong class="gold">Motivating Questions</strong>

<div class="font-large">

1. What programs am I <strong class="success">running</strong>?

2. How do I <strong class="danger">terminate</strong> a <strong
   class="primary">process</strong>?

</div>

---

# Processes: <strong class="gold">Attributes</strong>

<div class="columns-3-2">

<div class="centered">

<br>

<div class="alert warning-bg centered">

What programs am I <strong class="success">running</strong>?

</div>

A <strong class="primary">process</strong> is a <strong class="caution">____________________</strong>

instance of a <strong class="success">____________________</strong>.

</div>

<div>

<div class="centered">

<img src="static/img/slides03-processes-attributes.png">

</div>

</div>

</div>

Each <strong class="primary">process</strong> has:

<div class="columns">

<div>

- <strong>____________________</strong>

  <br>

- <strong>____________________</strong>

  <br>

- <strong>____________________</strong>

</div>

<div>

- <strong>____________________</strong>

  <br>

- <strong>____________________</strong>

  <br>

- <strong>____________________</strong>

</div>

</div>


---

# Processes: <strong class="gold">Signals</strong>

<br>

<div class="alert warning-bg centered">

How do I terminate a <strong class="primary">process</strong>?

</div>

<div class="centered">

<table class="bordered">
<thead class="danger-bg">
    <th>Signal Name</th>
    <th>Signal Number</th>
    <th>Operation</th>
</thead>
<tbody>
    <tr class="centered caution-bg font-large">
        <td><b></b></td>
        <td><b>2</b></td>
        <td>Interrupt the process</td>
    </tr>
    <tr class="centered warning-bg font-large">
        <td><b></b></td>
        <td><b>15</b></td>
        <td>Terminate the process</td>
    </tr>
    <tr class="centered danger-bg font-large">
        <td><b></b></td>
        <td><b>9</b></td>
        <td>Kill the process</td>
    </tr>
</tbody>
</table>

</div>

---

# I/O: <strong class="gold">Motivating Questions</strong>

<div class="font-large">

1. How do you <strong class="success">save</strong> the result of a command?

2. How do you <strong class="caution">ignore</strong> error messages?

</div>

---

# I/O: <strong class="gold">File Streams</strong>

<br>

<div class="alert warning-bg centered">

How do you <strong class="success">save</strong> the result of a command?

</div>

When a <strong class="primary">process</strong> is created, it automatically
has three <strong class="caution">file streams</strong>:

<div class="centered">

<br>

<img src="static/img/slides03-io-file-streams-blank.png">

</div>

---

# I/O: <strong class="gold">Pipelines</strong>

<br>

<div class="alert warning-bg centered">

How do you <strong class="caution">ignore</strong> error messages?

</div>

A <strong class="caution">pipe</strong> connects the <strong class="danger">____________________</strong> of the first <strong class="primary">process</strong> to

the <strong class="danger">____________________</strong> of the second <strong class="primary">process</strong>.

<div class="centered">

<br>

<img src="static/img/slides03-io-pipelines-blank.png" width="100%">

</div>
