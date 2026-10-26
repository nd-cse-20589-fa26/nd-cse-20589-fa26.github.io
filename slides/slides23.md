---
title: "Slides 23: I/O"
description: "I/O"
author: Peter Bui
keywords: lecture,sos,system calls,i/o
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides23.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## I/O

---

# Questions

<div class="font-large">

1. How do we copy <strong class="success">file</strong>'s data?

</div>

---

# I/O: <span class="gold">Overview</span>

<div class="columns">

<div>

All <strong class="warning">input</strong> and <strong
class="warning">output</strong> is performed on <strong
class="success">files</strong>:

1. <strong class="caution">Open</strong>

    Acquire handle to stream of data.

2. <strong class="caution">Close</strong>

    Release handle to stream of data.

</div>

<div>

3. <strong class="warning">Read</strong>

    Load chunk from stream of data.

4. <strong class="warning">Write</strong>

    Store chunk to stream of data.

5. <strong class="danger">Seek</strong>

    Move within stream of data.

</div>

</div>

---

# I/O: <span class="gold">Open / Close</span>

Using [os.open], we get a <strong class="caution">file descriptor</strong>,
which is a handle or reference to the stream of data.

```python
# Open file in read only mode and get file descriptor
try:
    rfd = os.open('/etc/hosts', os.O_RDONLY)
except OSError as e:
    print(e, file=sys.stderr)

# Close file descriptor
os.close(rfd)
```

[os.open]: https://docs.python.org/3/library/os.html#os.open

---

# I/O: <span class="gold">Read / Write</span>

To load data from a <strong class="caution">file descriptor</strong>, use
[os.read]:

```python
rfd  = os.open('data.txt', os.O_RDONLY) # Open file in read only mode
data = os.read(rfd, (1<<10))            # Read up to 1KB of data
```

To store data to a <strong class="caution">file descriptor</strong>, use
[os.write]:

```python
# Open file in write only mode and create it if necessary
wfd  = os.open('data.txt', os.O_WRONLY | os.O_CREAT)

# Write data to file descriptor
os.write(wfd, 'hello, world'.encode())  # Convert string to bytes
```

[os.read]: https://docs.python.org/3/library/os.html#os.read
[os.write]: https://docs.python.org/3/library/os.html#os.write

---

# I/O: [copy_file.py]

> Write a simplified version of [cp] that copies one file to another.

```bash
# Copy /etc/hosts to hosts.copy
$ ./copy_file.py /etc/hosts hosts.copy

# Verify that sha1sums are the same
$ sha1sum /etc/hosts hosts.copy
```

[cp]: https://man7.org/linux/man-pages/man1/cp.1.html
[copy_file.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides23/copy_file.py

---

# I/O: <span class="gold">Streams</span>

For **text files**, we usually want to *read one line at a time*.  For these
situations, we should use the high-level [open] function that wraps these
low-level <strong class="warning">system calls</strong> into a convenient [file
object] that act like <strong class="danger">streams</strong>:

```python
for line in open('/etc/hosts'):             # Use high-level file object stream
    print(line, end='')
```

If we already have a <strong class="caution">file descriptor</strong>, we can use [os.fdopen] or [open]
to convert it into a [file object]:

```python
rfd = os.open('/etc/hosts', os.O_RDONLY)    # Open file in read only mode
rfs = os.fdopen(rfd, 'r')                   # Convert file descriptor to stream
```

[os.fdopen]: https://docs.python.org/3/library/os.html#os.fdopen
[open]: https://docs.python.org/3/builtins/functions.html#open
[file object]: https://docs.python.org/3/glossary.html#term-file-object

---

# I/O: <span class="gold">Seek</span>

For some <strong class="danger">streams</strong>, we can move backwards and forwards using
[os.lseek]:

```python
rfd = os.open('/etc/hosts', os.O_RDONLY)    # Open file in read only mode

while data := os.read(rfd, (1<<10)):        # Read until end of file
    sys.stdout.write(data)

os.lseek(rfd, 0, os.SEEK_SET)               # Rewind to beginning of file

while data := os.read(rfd, (1<<10)):        # Read until end of file (again)
    sys.stdout.write(data)

os.close(rfd)                               # Close file descriptor
```

[os.lseek]: https://docs.python.org/3/library/os.html#os.lseek

---

# I/O: [file_array.py]

> Create a **persistent array** that supports the **index** operator.

<div class="columns-3-2">

<div>

```python
@dataclass
class FileArray:
    path:   str                 # Path to file/array
    size:   int=(1<<10)         # Size of file/array

    def __post_init__(self):
        ''' Post constructor: open file and allocate space. '''
        self.fd = os.open(self.path, os.O_RDWR | os.O_CREAT, 0o644)
        os.posix_fallocate(self.fd, 0, self.size)

    def __del__(self):
        ''' Destructor: close file '''
        os.close(self.fd)
```

</div>

<div>

```python
    def __getitem__(self, key: int) -> bytes:
        ''' Get item at key '''
        if key >= self.size:
            raise IndexError

        os.lseek(self.fd, key, os.SEEK_SET)
        return os.read(self.fd, 1)

    def __setitem__(self, key: int, value: bytes):
        ''' Set item at key with value '''
        if key >= self.size:
            raise IndexError

        os.lseek(self.fd, key, os.SEEK_SET)
        os.write(self.fd, value)
```

</div>

</div>

[file_array.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides23/file_array.py
