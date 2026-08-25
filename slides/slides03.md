---
title: "Slides 03: Files, Processes, I/O"
description: "Files, Processes, I/O"
author: Peter Bui
keywords: lecture,sos,files,processes,io
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides03.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Files, Processes, I/O

---

<!-- _class: lead -->

# Files

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

Where is <strong class="primary">ls</strong> located?

<strong class="hljs-comment">Ask the shell</strong><br>
$ **which** ls

<strong class="hljs-comment">Verify</strong><br>
$ **ls** /bin

<br>

<div class="centered">

The unix <strong class="primary">file system</strong> is structured as a
<strong class="success">hierarchical tree</strong> ([man 7 hier]).

</div>

[man 7 hier]:   https://man7.org/linux/man-pages/man7/hier.7.html
[inode]:        https://man7.org/linux/man-pages/man7/inode.7.html


</div>

<div>

<br>

<img src="static/img/slides03-files-hierarchy.png">

</div>

</div>

---

# Files: <strong class="gold">Home</strong>

<div class="columns">

<div class="centered">

<br>

<img src="static/img/slides03-files-home.png">

</div>

<div>

Typically, every user has a <strong class="success">home</strong> directory
where their personal files are stored:

- <strong class="caution">Directories</strong> and <strong
  class="caution">files</strong> that being with `.` are hidden by convention
  (aka <strong class="special">dotfiles</strong>)

- There are multiple ways to reference the <strong
  class="success">home</strong> directory:

    - `~/`
    - `~username/`
    - `$HOME`

</div>

</div>

---

# Files: <strong class="gold">Paths</strong>

<div class="columns-3-2">

<div>

<strong class="danger">Absolute paths</strong> always begin with the <strong
class="info">root</strong> directory:

$ **/bin/ls** <strong class="hljs-comment"># Absolute</strong>

<br>

<strong class="success">Relative paths</strong> are based on the <strong class="caution">current working
directory</strong>:

$ **../../../../bin/ls**    <strong class="hljs-comment"># Relative</strong>

</div>

<div>

<br>

<div class="alert caution-bg font-small">

<strong class="success">&nbsp;.</strong> Refers to **current directory**.

<strong class="success">..</strong> Refers to **parent directory**.

</div>

```bash
# Demonstration

$ cd /      # Absolute
$ bin/ls    # Relative
$ cd bin    # Relative
$ ./ls      # Relative
```

</div>

</div>

---

# Files: <strong class="gold">Metadata</strong>

<div class="columns">

<div>

How large is my <strong class="caution">~/.bashrc</strong>?

<strong class="hljs-comment">Use ls</strong><br>
$ **ls** -l ~/.bashrc

<strong class="hljs-comment">Use stat</strong><br>
$ **stat** ~/.bashrc

<strong class="hljs-comment">Use du</strong><br>
$ **du** -h ~/.bashrc

</div>

<div>

Every <strong class="success">file system object</strong> is represented by a
<strong class="danger">data structure</strong> called an <strong
class="caution">inode</strong>.

<div class="centered">

<br>

<img src="static/img/slides03-files-inode.png">

</div>

</div>

</div>

---

# Files: <strong class="gold">Permissions</strong>

<div class="columns">

<div>

How do I <strong class="danger">prevent</strong> people from reading my work?

<strong class="hljs-comment">Use chmod with octal</strong><br>
$ **chmod** 600 work

```
Classes:    Owner   Group   Other
Symbols:    rw-     ---     ---
Octal:      110     000     000     = 600
```

<strong class="hljs-comment">Use chmod with symbols</strong><br>
$ **chmod** u+rw,g=,o= work

</div>

<div>

A file's <strong class="info">mode</strong> specifies access permissions for
<strong class="success">user</strong>, <strong class="caution">group</strong>,
and <strong class="warning">other</strong> classes:

<div class="font-smaller">

- First symbol in the <strong class="info">mode</strong> mode represents type
  (**d = directory, - = regular, etc.**)

- This is followed by three triplets that represent the **permissions** for
  each class:

    - **r**: <strong class="info">readable</strong> by class
    - **w**: <strong class="danger">writable</strong> by class
    - **x**: <strong class="success">executable</strong> by class

</div>

</div>

</div>

---

# Files: <strong class="gold">Searching</strong>

Where did I put that <strong class="warning">.c</strong> file?

<strong class="hljs-comment">Use find</strong><br>
$ **find** . -name <strong class="danger">'*.c'</strong>

<strong class="hljs-comment">Use find (only files)</strong><br>
$ **find** . -type f -name <strong class="danger">'*.c'</strong>

<strong class="hljs-comment">Use find (only empty files)</strong><br>
$ **find** . -type f -empty -name <strong class="danger">'*.c'</strong>

<strong class="hljs-comment">Use find (only executable files)</strong><br>
$ **find** . -type f -executable -name <strong class="danger">'*.c'</strong>

---

<!-- _class: lead -->

# Processes

---

# Processes: <strong class="gold">Motivating Questions</strong>

<div class="font-large">

1. What programs am I <strong class="success">running</strong>?

2. How do I <strong class="danger">terminate</strong> a <strong
   class="primary">process</strong>?

</div>

---

# Processes: <strong class="gold">Attributes</strong>

<div class="columns">

<div>

What programs am I <strong class="success">running</strong>?

<strong class="hljs-comment">List processes</strong><br>
$ **ps** ux &nbsp;<strong class="hljs-comment"># User processes</strong><br>
$ **ps** aux <strong class="hljs-comment"># All processes</strong>

<strong class="hljs-comment">Watch processes</strong><br>
$ **top** &nbsp;<strong class="hljs-comment"># Interactive</strong><br>
$ **htop** <strong class="hljs-comment"># Colorful</strong>

<strong class="hljs-comment">Search Processes</strong><br>
$ **ps** ux | **grep** process-name<br>
$ **pgrep** process-name<br>

</div>

<div>

<div class="centered">

<img src="static/img/slides03-processes-attributes.png">

</div>

A <strong class="primary">process</strong> is a <strong
class="caution">loaded</strong> instance of a <strong
class="success">program</strong>.  Each process has:

<div class="font-small">

- Process ID (PID)

- Parent Process ID (PPID)

- UID / GUID

- Priority

- Terminal / TTY

</div>

</div>

</div>

---

# Processes: <strong class="gold">Signals</strong>

<div class="columns">

<div>

How do I terminate a <strong class="primary">process</strong>?

<strong class="hljs-comment">Send Interrupt Signal</strong><br>
**Control-C**

<strong class="hljs-comment">Send Terminate Signal</strong><br>
$ **kill** PID<br>
$ **pkill** process-name

<strong class="hljs-comment">Send Kill Signal</strong><br>
$ **kill** -9 PID<br>
$ **pkill** -9 process-name

</div>

<div class="font-small">

<table class="bordered">
<thead class="danger-bg">
    <th>Signal Name</th>
    <th>Signal Number</th>
    <th>Operation</th>
</thead>
<tbody>
    <tr class="centered">
        <td><b>TERM</b></td>
        <td><b>15</b></td>
        <td>Terminate the process</td>
    </tr>
    <tr class="centered">
        <td><b>INT</b></td>
        <td><b>2</b></td>
        <td>Interrupt the process</td>
    </tr>
    <tr class="centered">
        <td><b>KILL</b></td>
        <td><b>9</b></td>
        <td>Kill the process</td>
    </tr>
</tbody>
</table>

</div>

</div>

---

# Processes: <strong class="gold">Job Controls</strong>

With interactive <strong class="primary">processes</strong>, you have <strong class="success">job
controls</strong>:

<div class="columns-1-3">

<div class="font-smaller">

$ **sleep** 60 &<br>
[1] 23213

$ **jobs**<br>
[1]+ Running

$ **fg**<br>
sleep 60<br>
^Z<br>
[1]+ Stopped

$ **bg**<br>
[1]+ sleep 60 &

$ **kill** %1<br>
[1]+ Terminated

</div>

<div class="font-smaller">

<strong class="hljs-comment"># Execute sleep in the background</strong><br>
<br>

<strong class="hljs-comment"># List jobs</strong><br>
sleep 60 &<br>

<strong class="hljs-comment"># Bring job to foreground</strong><br>
<br>
<strong class="hljs-comment"># Suspend job</strong><br>
sleep 60<br>

<strong class="hljs-comment"># Background job</strong><br>
<br>

<strong class="hljs-comment"># Kill job</strong><br>
sleep 60<br>

</div>

</div>

---

<!-- _class: lead -->

# I/O

---

# I/O: <strong class="gold">Motivating Questions</strong>

<div class="font-large">

1. How do you <strong class="success">save</strong> the result of a command?

2. How do you <strong class="caution">ignore</strong> error messages?

</div>

---

# I/O: <strong class="gold">Redirection</strong>

<div class="columns-2-3">

<div>

How do you <strong class="success">save</strong> the result of a command?

<strong class="hljs-comment">Redirect stdout</strong><br>
$ **command** > output

<strong class="hljs-comment">Pipe stdout to tee</strong><br>
$ **command** | **tee** output

</div>

<div class="font-small">

<table class="bordered">
<thead class="danger-bg">
    <th width="200">Operation</td>
    <th>Syntax</td>
</thead>
<tbody>
    <tr class="centered">
        <td>Redirect <b>standard out</b></td>
        <td>&gt; file</td>
    </tr>
    <tr class="centered">
        <td>Redirect <b>standard out</b> and <b>error</b></td>
        <td class="centered">&gt; file 2&gt;&1 or &&gt; file</td>
    </tr>
    <tr class="centered">
        <td>Redirect <b>standard input</b></td>
        <td>&lt; file</td>
    </tr>
    <tr class="centered">
        <td>Redirect <b>standard output</b> to another command</td>
        <td><b>command1</b> | <b>command2</b></td>
    </tr>
    <tr class="centered">
        <td>Append <b>standard out</b></td>
        <td>&gt;&gt; file</td>
    </tr>
</tbody>
</table>

</div>

</div>

---

# I/O: <strong class="gold">File Streams</strong>

When a <strong class="primary">process</strong> is created, it automatically
has three <strong class="caution">file streams</strong>: <strong
class="danger">STDIN (0)</strong>, <strong class="danger">STDOUT (1)</strong>,
<strong class="danger">STDERR (2)</strong>

<div class="centered">

<br>

<img src="static/img/slides03-io-file-streams.png">

</div>

The parent of the created <strong class="primary">process</strong> (usually the
<strong class="danger">$SHELL</strong>) can redirect any of these files to
another file.

```bash
# Demonstration
$ sleep 60 < /etc/hosts > output
$ ls -l /proc/$(pgrep sleep)/fd
```

---

# I/O: <strong class="gold">Pipelines</strong>

A <strong class="caution">pipe</strong> connects the <strong
class="danger">standard output</strong> of the first <strong
class="primary">process</strong> to the <strong class="danger">standard
input</strong> of the second <strong class="primary">process</strong>.

<div class="centered">

<br>

<img src="static/img/slides03-io-pipelines.png">

</div>

---

# I/O: <strong class="gold">Examples</strong>

<strong class="hljs-comment">Redirect stdout and stderr to separate files</strong><br>
$ **find** /etc -type d > output 2> errors

<strong class="hljs-comment">Redirect both stdout and stderr to same file</strong><br>
$ **find** /etc -type d > combined 2>&1<br>
$ **find** /etc -type d &> combined

<strong class="hljs-comment">Redirect stderr to stdout, then stdout to file</strong><br>
$ **find** /etc -type d 2>&1 > output<br>

<strong class="hljs-comment">Redirect both stdout and stderr to tee program</strong><br>
$ **find** /etc -type d 2>&1 | **tee** combined<br>

<strong class="hljs-comment">Redirect stderr to blackhole and stdout to tee program</strong><br>
$ **find** /etc -type d 2> /dev/null | **tee** output<br>
