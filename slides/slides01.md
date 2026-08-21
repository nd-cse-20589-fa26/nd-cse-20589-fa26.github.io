---
title: "Lecture 01: Unix Programming Environment"
description: "Unix Programming Environment"
author: Peter Bui
keywords: lecture,sos,unix,shell
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides01.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Unix Programming Environment

---

# Unix Programming Environment

"You should keep in mind that whatever you're doing with the <strong
class="caution">shell</strong>, you're <strong
class="success">programming</strong> it - that’s largely why it works so well."

<div class="centered">

<img class="framed" src="https://m.media-amazon.com/images/I/61qUmPreFWL._AC_UF1000,1000_QL80_.jpg" width="320">

</div>

---

# UPE: <strong class="gold">Shell</strong>

<div class="columns-3-2">

<div>

<strong class="hljs-comment">To login to a student machine</strong><br>
**ssh** netid@student10.cse.nd.edu

<strong class="hljs-comment">List environment variables</strong><br>
**env**

<strong class="hljs-comment">Display value of SHELL variable</strong><br>
**echo** $SHELL

<strong class="hljs-comment">Set value of variable</strong><br>
NAME=VALUE

<strong class="hljs-comment">Export variable for sub-processes</strong><br>
**export** NAME

</div>

<div>

<div class="alert caution-bg centered font-smaller">

The <strong class="primary">unix shell</strong> is an <strong
class="success">interpreter</strong>: a program that <strong
class="caution">translates</strong> commands into actions <strong
class="special">on-the-fly</strong>.

</div>

<br>

<div class="alert info-bg font-smaller">

**Important Variables**:

<div class="font-small">

- <strong class="danger">PATH</strong>: Which directories to search for
  programs.

- <strong class="danger">LD_LIBRARY_PATH</strong>: Which directories to search
  for libraries.

- <strong class="danger">PYTHONPATH</strong>: Which directories to search for
  Python packages.

</div>

</div>

</div>

</div>

---

# UPE: <strong class="gold">Shell Configuration</strong>

<div class="columns-3-2">

<div>

<strong class="hljs-comment">Create alias for command</strong><br>
**alias** ll='ls -l'

<strong class="hljs-comment">Edit ~/.bashrc to store alias</strong><br>
**vim** ~/.bashrc

</div>

<div>

<div class="alert caution-bg centered font-smaller">

The <strong class="primary">unix shell</strong> can be customized by modifying
the <strong class="danger">~/.bashrc</strong> settings file which is loaded
every time you login.

</div>

</div>

</div>

<strong class="hljs-comment">Load settings from ~/.bashrc into current shell session</strong><br>
**source** ~/.bashrc

---

# UPE: <strong class="gold">User Information</strong>

<div class="columns-3-2">

<div>

<strong class="hljs-comment">View user name, groups</strong><br>
**whoami**<br>
**id**

<strong class="hljs-comment">List users on the current machine</strong><br>
**w**<br>
**who**

<strong class="hljs-comment">Become another user</strong><br>
**su** username

</div>

<div>

<div class="alert caution-bg centered font-smaller">

In the <strong class="primary">unix shell</strong> each <strong class="success">user</strong> has a
<strong class="caution">uid</strong> (<strong class="muted"><i>user</i></strong>) and a
<strong class="caution">gid</strong> (<strong class="muted"><i>group</i></strong>).

</div>

<br>

<div class="alert danger-bg centered font-smaller">

<strong class="danger">Note</strong>: You do not have <strong
class="danger">sudo privileges</strong> on the **student machines**, so <strong
class="danger">do not use</strong> this command in this environment!

</div>

</div>

</div>

<strong class="hljs-comment">Perform command with elevated privileges</strong><br>
**sudo** command


---

# UPE: <strong class="gold">System Properties</strong>

<div class="columns-3-2">

<div>

<strong class="hljs-comment">Display name of the machine</strong><br>
**hostname**

</div>

<div>

<div class="alert caution-bg centered font-smaller">

In the <strong class="primary">unix shell</strong>, you can <strong
class="success">query</strong> information about the current <strong
class="caution">computer system</strong>.

</div>

</div>

</div>

<strong class="hljs-comment">Display operating system and architecture</strong><br>
**uname** -a

<strong class="hljs-comment">See how long this machine has been running</strong><br>
**uptime**

<strong class="hljs-comment">View the network address of the machine</strong><br>
**ip** addr<br>
**ip** -br addr


---

# UPE: <strong class="gold">Navigation</strong>


<div class="columns-3-2">

<div>

<strong class="hljs-comment">Print current working directory</strong><br>
**pwd**

<strong class="hljs-comment">List contents of directory</strong><br>
**ls**

<strong class="hljs-comment">Go into directory</strong><br>
**cd** tmp

<strong class="hljs-comment">Go to previous directory</strong><br>
**cd** -

</div>

<div>

<div class="alert caution-bg centered font-smaller">

The <strong class="primary">unix filesystem</strong> is a <strong class="success">hierarchical
structure</strong>: files and directories are <strong class="danger">nested</strong> inside
other directories.

</div>

<br>

<div class="alert info-bg font-smaller">

**Notable Directory Symbols**:

&nbsp;<strong class="gold">~</strong> Home directory

&nbsp;<strong class="gold">.</strong> Current directory

<strong class="gold">..</strong> Parent directory

</div>

</div>

</div>

---

# UPE: <strong class="gold">Help</strong>

<div class="columns-3-2">

<div>

<strong class="hljs-comment">View manual for ls</strong><br>
**man** ls

<strong class="hljs-comment">View usage message for ls</strong><br>
**ls** --help

<strong class="hljs-comment">View summarized manual for ls</strong><br>
**tldr** ls

</div>

<div>

<div class="alert caution-bg centered font-smaller">

The <strong class="primary">unix programming environment</strong> implements the
<strong class="success">POSIX standard</strong>, which is a set of common utilities and
commands found on most <strong class="danger">BSD</strong>, <strong class="caution">Linux</strong>,
<strong class="special">macOS</strong>, and <strong class="info">Windows (WSL)</strong>.

</div>

</div>

</div>

---

# UPE: <strong class="gold">File Management</strong>

<div class="columns-3-2">

<div>

<strong class="hljs-comment">Copy from source to target</strong><br>
**cp** source target

<strong class="hljs-comment">Move from source to target</strong><br>
**mv** source target

<strong class="hljs-comment">Create target or update timestamp</strong><br>
**touch** target

<strong class="hljs-comment">Remove source</strong><br>
**rm** source

<strong class="hljs-comment">Remove directory</strong><br>
**rm** -rf directory

</div>

<div>

<div class="alert caution-bg font-smaller">

<div class="centered">

The <strong class="primary">unix shell</strong> supports <strong
class="success">globbing</strong> patterns:

</div>

`*` match any number of characters.

`?` match a single character.

`[set]` match any character inside brackets.

</div>

</div>

</div>

---

# UPE: <strong class="gold">File Properties</strong>

<div class="columns-3-2">

<div>

<strong class="hljs-comment">View contents of a file</strong><br>
**cat** file
**less** file

<strong class="hljs-comment">View metadata of file</strong><br>
**stat** file

</div>

<div>

<div class="alert caution-bg centered font-smaller">

In the <strong class="primary">unix programming environment</strong>, each
<strong class="success">file</strong> or <strong
class="success">directory</strong> has a set of associated <strong
class="caution">metadata</strong>.

</div>

</div>

</div>

<strong class="hljs-comment">Change the permissions (mode) of a file (make it executable)</strong><br>
**chmod** +x target

---

# UPE: <strong class="gold">File Utilities</strong>

<div class="columns-3-2">

<div>

<strong class="hljs-comment">Compare two files</strong><br>
**diff** original other

<strong class="hljs-comment">Count the number of files in a file</strong><br>
**wc** -l file

<strong class="hljs-comment">Compute the checksum of a file</strong><br>
**sha1sum** file

<strong class="hljs-comment">Sort the contents of a file</strong><br>
**sort** file

<strong class="hljs-comment">Generate a sequence</strong><br>
**seq** start end

</div>

<div>

<div class="alert caution-bg centered font-smaller">

The <strong class="primary">unix programming environment</strong> has a number
of <strong class="success">standard utilities</strong>.

</div>

</div>

</div>

---

# UPE: <strong class="gold">Text Editors</strong>

<div class="columns-3-2">

<div class="slide-centered">

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Gnu-nano.svg/250px-Gnu-nano.svg.png">

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Vimlogo.svg/250px-Vimlogo.svg.png">

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/EmacsIcon.svg/250px-EmacsIcon.svg.png">

</div>

<div>

<div class="alert caution-bg centered font-smaller">

The <strong class="primary">unix programming environment</strong> supports many
<strong class="success">text editors</strong>.

</div>

</div>

</div>

---

# UPE: <strong class="gold">Processes</strong>

<div class="columns-3-2">

<div>

<strong class="hljs-comment">List processes</strong><br>
**ps** &nbsp;&nbsp;&nbsp; <strong class="hljs-comment">Current user session</strong><br>
**ps** ux&nbsp; <strong class="hljs-comment">User processes</strong><br>
**ps** aux <strong class="hljs-comment">All processes on system</strong><br>

<strong class="hljs-comment">Signal a process by identifier</strong><br>
**kill** pid

<strong class="hljs-comment">Signal a process by name</strong><br>
**pkill** name<br>
killall name

</div>

<div>

<div class="alert caution-bg centered font-smaller">

The <strong class="primary">unix programming environment</strong> represents
<strong class="caution">running instances of programs</strong> as <strong
class="success">processes</strong>.

</div>

</div>

</div>

---

# UPE: <strong class="gold">Session</strong>

<div class="columns-3-2">

<div>

<strong class="hljs-comment">List jobs</strong><br>
**jobs**

<strong class="hljs-comment">Suspend current foreground</strong><br>
**Control-Z**

</div>

<div>

<div class="alert caution-bg centered font-smaller">

Within a <strong class="primary">unix shell session</strong>, you can control
multiple <strong class="success">processes</strong> as separate <strong
class="caution">jobs</strong>.

</div>

</div>

</div>

<strong class="hljs-comment">Allow suspended job to run in the background</strong><br>
**bg**

<strong class="hljs-comment">Bring background job to the foreground</strong><br>
**fg**

---

# UPE: <strong class="gold">I/O</strong>

<div class="columns-3-2">

<div>

<strong class="hljs-comment">Save output of command to a file</strong><br>
**command** > output.file

<strong class="hljs-comment">Save errors of command to a file</strong><br>
**command** 2> errors.file

</div>

<div>

<div class="alert caution-bg centered font-smaller">

In the <strong class="primary">unix programming environment</strong>, each
<strong class="success">process</strong> has <strong class="caution">standard
file streams</strong>: <strong class="danger">input</strong>, <strong
class="danger">output</strong>, <strong class="danger">error</strong>.

</div>

</div>

</div>

<strong class="hljs-comment">Save both output and errors of a command to a file</strong><br>
**command** &> combined.file<br>
**command** > output.file 2>&1

<strong class="hljs-comment">Stream contents of file into a command as input</strong><br>
command < input.file

---

# UPE: <strong class="gold">Pipelines</strong>

<div class="columns-3-2">

<div>

<strong class="hljs-comment">Stream the output of one command into another</strong><br>
**command1** | **command2**

</div>

<div>

<div class="alert caution-bg centered font-smaller">

In the <strong class="primary">unix programming environment</strong>, multiple
<strong class="success">processes</strong> can be connected together using
<strong class="caution">pipes</strong> to create <strong
class="danger">pipelines</strong>.

</div>

</div>

</div>

<br>

<div class="centered">
<img src="static/img/slides01-pipeline.png" width="900">
</div>

---

# UPE: <strong class="gold">Filters</strong>

<div class="columns-3-2">

<div class="font-smaller">

<strong class="hljs-comment">Display first few lines of stream</strong><br>
**command** | **head**

<strong class="hljs-comment">Display last few lines of stream</strong><br>
**command** | **tail**

<strong class="hljs-comment">Search contents of a stream</strong><br>
**command** | **grep** query

<strong class="hljs-comment">Extract delimited fields in a stream</strong><br>
**command** | **cut** -d , -f 1<br>
**command** | **awk** -F , '{print $1}'

<strong class="hljs-comment">Translate contents of a stream</strong><br>
**command** | **tr** set1 set2

<strong class="hljs-comment">Modify contents of a stream</strong><br>
**command** | **sed** '...'</strong><br>

</div>

<div>

<div class="alert caution-bg centered font-smaller">

In the <strong class="primary">unix programming environment</strong>, there are
a variety of <strong class="success">filters</strong> that <strong
class="caution">process streams of text</strong>.

</div>

</div>

</div>

---

# UPE: <strong class="gold">Unix Philosophy</strong>

<div class="slide-centered font-large">

<strong class="success">This is the Unix Philosophy</strong>

Write programs that do <strong class="caution">one thing</strong> and <strong
class="caution">do it well</strong>.

Write programs to <strong class="caution">work together</strong>.

Write programs to handle <strong class="caution">text streams</strong>, because
that is a universal interface.

</div>
