---
title: "Slides 06: Files, Processes, Requests"
description: "Files, Processes, Requests"
author: Peter Bui
keywords: lecture,sos,python,files, processes, requests
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides06.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Files, Processes, Requests

---

<!-- _class: lead -->

# Files

---

# Files: <span class="gold">Paths</span>

<strong class="success">Python</strong> provides many <strong
class="primary">file system</strong> related functions in the [os] package.

```python
# Form path to README.md in current working directory
>>> path = os.path.join(os.curdir, 'README.md')
>>> path
'./README.md'

# Get absolute path
>>> os.path.abspath(path)
'/escnfs/home/pbui/src/teaching/cse.20589.fa26/assignments-pbui/homework02/README.md'

# Check if path exists
>>> os.path.exits(path)
True
```

[os]: https://docs.python.org/3/library/os.html

---

# Files: <span class="gold">Checks</span>

As we can in <strong class="primary">bash</strong>, we can perform checks on a
<strong class="primary">file</strong>:

<table class="bordered font-smaller">
<thead>
    <th class="caution-bg">Unix Command</th>
    <th class="success-bg">Python Function</th>
    <th class="info-bg">Description</th>
</thead>
<tbody>
<tr>
    <td class="caution-bg">test -e $p</td>
    <td class="success-bg">os.path.exists(p)</td>
    <td class="info-bg">Checks if p exists</td>
</tr>
<tr>
    <td class="caution-bg">test -d $p</td>
    <td class="success-bg">os.path.isdir(p)</td>
    <td class="info-bg">Checks if p is a directory</td>
</tr>
<tr>
    <td class="caution-bg">test -f $p</td>
    <td class="success-bg">os.path.isfile(p)</td>
    <td class="info-bg">Checks if p is a regular file</td>
</tr>
<tr>
    <td class="caution-bg">test -r $p</td>
    <td class="success-bg">os.access(p, os.R_OK)</td>
    <td class="info-bg">Checks if p is readable</td>
</tr>
<tr>
    <td class="caution-bg">test -w $p</td>
    <td class="success-bg">os.access(p, os.W_OK)</td>
    <td class="info-bg">Checks if p is writable</td>
</tr>
<tr>
    <td class="caution-bg">test -x $p</td>
    <td class="success-bg">os.access(p, os.x_OK)</td>
    <td class="info-bg">Checks if p is executable</td>
</tr>
</tbody>
</table>

---

# Files: <span class="gold">Properties</span>

Likewise, we can examine properties of a <strong class="primary">file</strong>:

<table class="bordered font-smaller">
<thead>
    <th class="success-bg">Python Function</th>
    <th class="info-bg">Information</th>
</thead>
<tbody>
<tr>
    <td class="success-bg">os.path.basename(p)</td>
    <td class="info-bg">File Name</td>
</tr>
<tr>
    <td class="success-bg">os.path.dirname(p)</td>
    <td class="info-bg">Directory Name</td>
</tr>
<tr>
    <td class="success-bg">os.path.abspath(p)</td>
    <td class="info-bg">Absolute Path</td>
</tr>
<tr>
    <td class="success-bg">os.path.realpath(p)</td>
    <td class="info-bg">Canonical Path</td>
</tr>
<tr>
    <td class="success-bg">os.path.getmtime(p)</td>
    <td class="info-bg">Modification Time</td>
</tr>
<tr>
    <td class="success-bg">os.path.getsize(p)</td>
    <td class="info-bg">File Size</td>
</tr>
<tr>
    <td class="success-bg">os.path.splitext(p)[-1]</td>
    <td class="info-bg">File Extension</td>
</tr>
</table>

---

# Files: <span class="gold">Actions</span>

Finally, we can perform actions on the <strong class="primary">file
system</strong> using wrappers for <strong class="danger">system
calls</strong>:

<table class="bordered font-smaller">
<thead>
    <th class="caution-bg">Unix Command</th>
    <th class="success-bg">Python Function</th>
    <th class="info-bg">Description</th>
</thead>
<tbody>
<tr>
    <td class="caution-bg">pwd</td>
    <td class="success-bg">os.getcwd()</td>
    <td class="info-bg">Get current working directory</td>
</tr>
<tr>
    <td class="caution-bg">cd $p</td>
    <td class="success-bg">os.chdir(path)</td>
    <td class="info-bg">Change directory to path</td>
</tr>
<tr>
    <td class="caution-bg">ls $p</td>
    <td class="success-bg">os.listdir(path)</td>
    <td class="info-bg">List contents of path</td>
</tr>
<tr>
    <td class="caution-bg">chmod mode $p</td>
    <td class="success-bg">os.chmod(path, mode)</td>
    <td class="info-bg">Change mode of path</td>
</tr>
<tr>
    <td class="caution-bg">mv $src $dst</td>
    <td class="success-bg">os.rename(src, dst)</td>
    <td class="info-bg">Rename src to dst</td>
</tr>
<tr>
    <td class="caution-bg">rm $path</td>
    <td class="success-bg">os.unlink(path)</td>
    <td class="info-bg">Remove path</td>
</tr>
<tr>
    <td class="caution-bg">ln $src $dst</td>
    <td class="success-bg">os.link(src, dst)</td>
    <td class="info-bg">Create hard link from src to dst</td>
</tr>
<tr>
    <td class="caution-bg">ln -s $src $dst</td>
    <td class="success-bg">os.symlink(src, dst)</td>
    <td class="info-bg">Create soft link from src to dst</td>
</tr>
</tbody>
</table>

---

# Example: [which.py]

Write a <strong class="success">Python</strong> script that implements the
`which` command (ie. *searches the paths in the `PATH` environment variable for
the location of a program*).

```bash
$ ./which.py python3
/escnfs/home/pbui/pub/pkgsrc-2024Q2/bin/python3.12

$ ./which.py bash
/usr/bin/bash

$ ./which.py asdf
no asdf in (/escnfs/home/pbui/pub/pkgsrc/sbin:...)
```

[which.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides06/which.py

---

<!-- _class: lead -->

# Processes

---

# Processes: <span class="gold">Utilities</span>

<div class="columns">

<div>

We can execute a shell command by using [os.system]:


```python
# Execute ls -l
os.system('ls -l')
```

</div>

<div>

We can create a <strong class="caution">pipe</strong> to a command by using [os.popen]:

```python
# Execute and from ls -l
for line in os.popen('ls -l'):
    print(line.rstrip())
```

</div>

</div>

<br>

<div class="alert warning-bg centered font-smaller">

Both [os.system] and [os.popen] spawn a <strong class="primary">shell</strong>
to execute the given commands.  This means that these utility functions have
some extra overhead due to an additional <strong class="primary">shell</strong>
process.  However, the benefit of this approach is that users can do more
sophisticated commands such as <strong class="success">pipelines</strong>.

</div>

[os.system]: https://docs.python.org/3/library/os.html#os.system
[os.popen]: https://docs.python.org/3/library/os.html#os.popen

---

# Processes: <span class="gold">Subprocess</span>

For more fine-grained control of executing commands, <strong
class="success">Python</strong> provides the [subprocess] module:

<div class="columns">

<div>

```python
# Execute ls -l
subprocess.run(['ls', '-l'])
```

</div>

<div>

```python
# Execute and read from ls -l
process = subprocess.run(['ls', '-l'], capture_output=True)
stdout  = process.stdout.decode()
for line in stdout.splitlines():
    print(line.rstrip())
```

</div>

</div>

<br>

<div class="alert caution-bg centered font-smaller">

Although the [subprocess] functions tend to be more <strong
class="danger">complicated</strong> and <strong class="danger">verbose</strong>
than either [os.system] or [os.popen], the [subprocess] functions provide more
<strong class="success">flexibility</strong> and <strong
class="success">control</strong>.  For instance, you can redirect each of the
<strong class="danger">standard file streams</strong> to different targets
easily using [subprocess].  Additionally, you can have a command run in the
<strong class="warning">background</strong> with [subprocess].

</div>


[subprocess]: https://docs.python.org/3/library/subprocess.html#module-subprocess

---

# Example: [randomsay.py]

Write a <strong class="success">Python</strong> script that chooses a random
<strong class="caution">cow</strong> from [cowsay] and then runs the command with the chosen
<strong class="caution">cow</strong>.

```bash
$ ./randomsay.py hello, world
 ______________
< hello, world >
 --------------
        \  ^___^
         \ (ooo)\_______
           (___)\       )\/\
                ||----w |
                ||     ||
```

[cowsay]: https://github.com/cowsay-org/cowsay
[randomsay.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides06/randomsay.py

---

<!-- _class: lead -->

# Requests

---

# Requests: <span class="gold">Get</span>

To fetch data via [HTTP], we can use the [requests] package:

```python
>>> import requests                 # Import requests package

>>> url      = 'https://nd.edu'
>>> response = requests.get(url)    # Perform HTTP GET on url

>>> response.status_code            # View status code of response
200

>>> response.text                   # View text of response
'<!doctype html>\n...
```

[HTTP]: https://en.wikipedia.org/wiki/HTTP
[requests]: https://requests.readthedocs.io/en/latest/

---

# Requests: <span class="gold">Post</span>

To send data via [HTTP], we can use the [requests] package to do a `POST`:

```python
>>> url      = 'https://dredd.h4x0r.space/quiz/cse.20589.fa26/reading02'
>>> payload  = open('answers.json').read()      # Read payload data
>>> response = requests.post(url, data=payload) # Perform HTTP POST on url with data payload

>>> response.status_code                        # View status code of response
200

>>> response.text                               # View text of response
'{"q01": 4.0, "q02": 7.0, "q03": 4.0, "q04": 5.0,
  "score": 20.0, "value": 20.0, "status": 0,
  "points": {"q01": 4.0, "q02": 7.0, "q03": 4.0, "q04": 5.0}}'
```

---

# Requests: <span class="gold">Parameters and Headers</span>

We can use custom parameters and headers during a [HTTP] request by passing in
a [dict]:

```python
# Use Open Library API: https://openlibrary.org/developers/api
url      = 'https://openlibrary.org/search.json'
params   = {'q': 'In the beginning was the command line'}
headers  = {'User-Agent': 'SoftwareSystemsExample/0.1 (pbui@nd.edu)'}
response = requests.get(url, params=params, headers=headers)
print(response.text)
```

---

# Requests: <span class="gold">Timeouts</span>

We can specify a <strong class="warning">timeout</strong> when performing a
[HTTP] request to avoid waiting forever:

```python
url      = 'https://openlibrary.org/search.json'
params   = {'q': 'Lord of the Rings'}
headers  = {'User-Agent': 'SoftwareSystemsExample/0.1 (pbui@nd.edu)'}

try:
    # Wait at most 1 second
    response = requests.get(url, params=params, headers=headers, timeout=1)
except requests.exceptions.Timeout as e:
    print(f'Uh Oh: {e}')
```

[dict]: https://docs.python.org/3/library/stdtypes.html#dict

---

# Example: [catalog.py]

Write a <strong class="success">Python</strong> script that queries
[catalog.cse.nd.edu] and displays all the machines with the specified
attributes.

<div class="columns">

<div>

```bash
# Query all machines
$ ./catalog.py
...
chirp   ta-a6k-004.crc.nd.edu   unknown
chirp   ta-a6k-005.crc.nd.edu   unknown
chirp   ta-a6k-006.crc.nd.edu   unknown

# Query all machines that belong to dthain or ubuntu
$ ./catalog.py -o dthain -o ubuntu
...
chirp   d12chas324.crc.nd.edu   dthain
chirp   d12chas325.crc.nd.edu   dthain
chirp   d12chas326.crc.nd.edu   dthain
chirp   d12chas327.crc.nd.edu   dthain
vine_factory    ec2-100-53-140-130  ubuntu
```

</div>

<div>

```bash
# Query all machines of type wq_master or vine_factory
$ ./catalog.py -t wq_master,vine_factory
vine_factory    cclws23.cse.nd.edu      mislam5
vine_factory    condorfe.crc.nd.edu     bslydelg
...
wq_master       gauss.nmrbox.org        jaanderson
wq_master       glados.crc.nd.edu       rgoldouz
```

</div>

</div>

[catalog.cse.nd.edu]: https://catalog.cse.nd.edu
[catalog.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides06/catalog.py
