---
title: "Slides 22: Directories"
description: "Directories"
author: Peter Bui
keywords: lecture,sos,system calls,directories
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides22.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Directories

---

# Questions

<div class="font-large">

1. How do we list the contents of <strong class="caution">directory</strong>?

    a. Using <strong class="danger">recursion</strong>?
    b. Using <strong class="special">OOP</strong>?

</div>

---

# Directories: <span class="gold">Overview</span>

As with <strong class="success">files</strong>, <strong
class="caution">directories</strong> are also represented by <strong
class="special">inodes</strong> in the <strong class="warning">file
system</strong>.

- Each <strong class="caution">directory</strong> contains:

    - References to itself (`.`) and its <strong
      class="warning">parent</strong> (`..`)

    - References to other <strong class="special">inodes</strong> (ie. <strong
      class="comment">entries</strong>)

- Each <strong class="success">process</strong> tracks its
  <strong="caution">current working directory</strong>:

    ```python
    # Get current working directory of process
    >>> os.getcwd()
    ```

---

# Directories: <span class="gold">Operations</span>

Many of the <strong class="warning">file system</strong> operations we might
use <strong class="danger">unix commands</strong> for can be accomplished with
<strong class="success">Python</strong> functions:

<table class="bordered">
<thead>
    <th class="info-bg">Unix Command</th>
    <th class="success-bg">Python Function</th>
</thead>
<tbody>
<tr>
    <td class="info-bg">cd</td>
    <td class="success-bg">os.chdir(path)</td>
</tr>
<tr>
    <td class="info-bg">chmod</td>
    <td class="success-bg">os.chmod(path, mode)</td>
</tr>
<tr>
    <td class="info-bg">mkdir</td>
    <td class="success-bg">os.mkdir(path, mode)</td>
</tr>
<tr>
    <td class="info-bg">rm</td>
    <td class="success-bg">os.unlink(path)</td>
</tr>
<tr>
    <td class="info-bg">mv</td>
    <td class="success-bg">os.rename(path)</td>
</tr>
<tr>
    <td class="info-bg">cp</td>
    <td class="success-bg">shutil.copy(src, dst)</td>
</tr>
</tbody>
</table>

---

# Directories: <span class="gold">Listing</span>

To list the contents of a directory, we can use either [os.listdir] or
[os.scandir]:

<div class="columns">

<div>

```python
# List all entries under root directory along with size
for name in os.listdir(root):       # Strings
    path = os.path.join(root, name)
    print(f'{path} {os.path.getsize(path)}')
```
</div>

<div>

```python
# List all entries under root directory along with size
with os.scandir(root) as entries:   # DirEntry objects
    for entry in entries:
        print(f'{entry.path} {entry.stat().st_size}')
```

</div>
</div>

> Using [os.scandir] instead of [os.listdir] can significantly increase the
> performance of code that also needs file type or file attribute information.

[os.listdir]: https://docs.python.org/3/library/os.html#os.listdir
[os.scandir]: https://docs.python.org/3/library/os.html#os.scandir

---

# Directories: <span class="gold">Walking</span>

To <strong class="warning">walk</strong> a <strong
class="caution">directory</strong> tree, we can use the [os.walk] function,
which internally uses [os.scandir] <strong class="danger">recursively</strong>.

```python
# Walk the /etc directory and print out files and their sizes
for root, dirs, files in os.walk('/etc/'):
    for name in files:
        path = os.path.join(root, name)
        print(f'{path} {os.path.getsize(path)}')
```

Alternatively, we can use the [Path.walk] method to get [Path] objects instead
of just strings as we <strong class="warning">walk</strong> a <strong
class="caution">directory</strong>.

[os.walk]: https://docs.python.org/3/library/os.html#os.walk
[Path.walk]: https://docs.python.org/3/library/pathlib.html#pathlib.Path.walk
[Path]: https://docs.python.org/3/library/pathlib.html#concrete-paths

---

# Directories: [list_rec.py] (<i class="muted">Recursive</i>)

> Write a simplified version of [ls] that lists the files in directory
> (*possibly recursively*) along with the corresponding file sizes.

```
$ ./list_rec.py  -h
Usage: list [directory]
    -R      List the contents of all directories recursively
```

[ls]: https://man7.org/linux/man-pages/man1/ls.1.html

[list_rec.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides22/list_rec.py

---

# OOP: <span class="gold">Inheritance</span>

<strong class="warning">Inheritance</strong> is a core <strong
class="special">OOP principle</strong> that enables the creation of <strong
class="caution">hierarchical relationships</strong> between units to allow for
<strong class="success">code reuse</strong>.

<div class="columns">

<div>

```python
# PathEntry objects inherit all attributes and
# methods of Path class
class PathEntry(pathlib.Path):
    @property
    def path(self): # Add new method to PathEntry
        return self.parent / self

entry = PathEntry('/etc/hosts')
print(entry.name)   # From Path class
print(entry.path)   # From PathEntry class
```

</div>

<div>

```python
# Define abstract class or interface
@dataclass
class BaseWalker(ABC):
    entry: os.DirEntry | PathEntry
    @abstractmethod
    def walk(self, recursive: bool=False): pass

# Define concrete class that implements interface
class NoopWalker(BaseWalker):
    def walk(self, recursive: bool=False): pass
```

</div>

</div>

<br>

<div class="alert info-bg font-small">

To define an <strong class="special">interface</strong>, we can create an
[abstract base class] and mark [abstract methods] which need to be defined by
<strong class="caution">concrete classes</strong> that <strong
class="special">inherit</strong> from this `ABC`.

</div>

[abstract base class]: https://docs.python.org/3/library/abc.html
[abstract methods]: https://docs.python.org/3/library/abc.html#abc.abstractmethod

---

# OOP: <span class="gold">Factory Pattern</span>

The <strong class="special">factory design pattern</strong> uses a specialized
<strong class="special">factory</strong> method that produces **instantiated**
objects.  This is done to <strong class="success">abstract</strong> away
complex object instantiation logic.

<div class="columns-1-2">

<div class="font-small">

- <strong class="caution">Product</strong>: An interface or abstract class
  shared by all objects the **factory** produces.

- <strong class="warning">Concrete Products</strong>: Specific classes that
  implement <strong class="caution">product</strong> interface.

- <strong class="danger">Concrete Creator</strong>: Specific <strong
  class="special">factory</strong> method that returns <strong
  class="warning">concrete products</strong>.

</div>

<div>

```python
@dataclass
class BaseWalker:                                   # Product Interface (provides walk method)
    entry: os.DirEntry | PathEntry
    def walk(self, recursive: bool=False): pass

class FileWalker(BaseWalker):                       # Concrete Product (File)
    def walk(self, recursive: bool=False): print(f'{self.entry.path} {self.entry.stat().st_size}')

class DirectoryWalker(BaseWalker):                  # Concrete Product (Directory)
    def walk(self, recursive: bool=False):
        with os.scandir(self.entry.path) as entries:
            for entry in map(WalkerFactory.get_walker, entries, cycle([recursive])):
                entry.walk(recursive)

class WalkerFactory:                                # Concrete Creator
    @classmethod                                    # Factory method
    def get_walker(cls, entry: os.DirEntry | PathEntry, recursive: bool=False):
        match stat.S_IFMT(entry.stat().st_mode):
            case stat.S_IFREG: return FileWalker(entry)
            case stat.S_IFDIR: return DirectoryWalker(entry) if recursive else NoopWalker(entry)
            case _:            return NoopWalker(entry)
```

</div>

</div>

---

# Directories: [list_oop.py] (<i class="muted">OOP</i>)

> Write a simplified version of [ls] that lists the files in directory
> (*possibly recursively*) along with the corresponding file sizes.

```
$ ./list_oop.py  -h
Usage: list [directory]
    -R      List the contents of all directories recursively
```

[list_oop.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides22/list_oop.py
