---
title: "Slides 05: Data Structures, Arguments, I/O"
description: "Data Structures, Arguments, I/O"
author: Peter Bui
keywords: lecture,sos,python,data structures, arguments, i/o
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides05.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Data Structures, Arguments, I/O

---

<!-- _class: lead -->

# Data Structures

---

# Data Structures: <span class="gold">Overview</span>

<div class="slide-centered">

<table class="bordered">
<thead>
    <th>Container</th>
    <th>C</th>
    <th>Python</th>
    <th>Python Syntax</th>
</thead>
<tbody>
    <tr class="success-bg">
        <td class="centered">Sequence</td>
        <td class="centered">DynamicArray, LinkedList</td>
        <td class="centered">List</td>
        <td class="centered">[a, b]</td>
    </tr>
    <tr class="caution-bg">
        <td class="centered">Fixed</td>
        <td class="centered">Array</td>
        <td class="centered">Tuple</td>
        <td class="centered">(a, b)</td>
    </tr>
    <tr class="warning-bg">
        <td class="centered">Membership</td>
        <td class="centered">ArraySet, ListSet, BitSet</td>
        <td class="centered">Set</td>
        <td class="centered">{a, b}</td>
    </tr>
    <tr class="danger-bg">
        <td class="centered">Associative</td>
        <td class="centered">HashTable</td>
        <td class="centered">Dict</td>
        <td class="centered">{a: 0, b: 1}</td>
    </tr>
</tbody>
</table>

</div>

---

# Data Structures: <span class="gold">Lists</span>

To create a <strong class="success">sequence</strong> of <strong
class="primary">objects</strong>, we can use a [list], which internally is a
<strong class="primary">dynamic array</strong>.

<table class="bordered">
<thead>
    <th class="info-bg">Operation</th>
    <th class="caution-bg">C</th>
    <th class="success-bg">Python</th>
</thead>
<tbody>
<tr>
    <td class="info-bg font-small">Create empty array</td>
    <td class="caution-bg font-small">Array *array = array_create()</td>
    <td class="success-bg font-small">array = []</td>
</tr>
<tr>
    <td class="info-bg font-small">Get size of array</td>
    <td class="caution-bg font-small">array->size</td>
    <td class="success-bg font-small"><b>len</b>(array)</td>
</tr>
<tr>
    <td class="info-bg font-small">Add to back of array</td>
    <td class="caution-bg font-small">array_append(array, value)</td>
    <td class="success-bg font-small">array.append(value)</td>
</tr>
<tr>
    <td class="info-bg font-small">Insert into array</td>
    <td class="caution-bg font-small">array_insert(array, index, value)</td>
    <td class="success-bg font-small">array.insert(index, value)</td>
</tr>
<tr>
    <td class="info-bg font-small">Remove from array</td>
    <td class="caution-bg font-small">array_pop(array, index)</td>
    <td class="success-bg font-small">array.pop(index)</td>
</tr>
</tbody>
</table>

<br>

<div class="alert info-bg centered">

**Note**: <strong class="success">Python</strong> [lists] support <strong
class="danger">negative indices</strong>.

</div>

[list]: https://docs.python.org/3/library/stdtypes.html#list
[lists]: https://docs.python.org/3/library/stdtypes.html#list

---

# Data Structures: <span class="gold">Lists</span> (<span class="muted">*Examples*</span>)

<div class="columns">

<div>

```python
# Create list
>>> data = ['Leonardo', 'Donatello',
'Raphael', 'Michelangelo']

# Get size of list
>>> len(data)
4

# Get first item
>>> data[0]
'Leonardo'

# Get last item
>>> data[-1]
'Michelangelo'
```

</div>

<div>

```python
# Add 'Splinter' to list
>>> data.append('Splinter')
>>> data
['Leonardo', 'Donatello', 'Raphael',
 'Michelangelo', 'Splinter']

# Remove 'Leonardo' from list
>>> data.pop(0)
>>> data
['Donatello', 'Raphael',
 'Michelangelo', 'Splinter']
```

</div>

</div>

---

# Data Structures: <span class="gold">Tuples</span>

To create an <strong class="danger">immutable</strong> <strong
class="success">sequence</strong> of <strong class="primary">objects</strong>,
we can use a [tuple], which is similar to a <strong class="primary">normal
array</strong> in <strong class="danger">C</strong>.

```python
>>> data = ('Huey', 'Dewey', 'Louie')	        # Create tuple
>>> len(data)                                   # Get length of tuple
3

>>> data[1]                                     # Get first item
'Dewey'

>>> data[1] = 'Launchpad'                       # Try to change first item
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

[tuple]: https://docs.python.org/3/library/stdtypes.html#tuple

---

# Data Structures: <span class="gold">Strings</span>

To create an <strong class="danger">immutable</strong> <strong
class="success">sequence</strong> of **characters**, we can use a [string]
(*which are not `NUL` terminated*):

<table class="bordered">
<thead>
    <th class="info-bg">Operation</th>
    <th class="caution-bg">C</th>
    <th class="success-bg">Python</th>
</thead>
<tbody>
<tr>
    <td class="info-bg font-small">Create a string</td>
    <td class="caution-bg font-small">char s[] = "hello"</td>
    <td class="success-bg font-small">s = "hello"</td>
</tr>
<tr>
    <td class="info-bg font-small">Get length of string</td>
    <td class="caution-bg font-small">strlen(s)</td>
    <td class="success-bg font-small">len(s)</td>
</tr>
<tr>
    <td class="info-bg font-small">Lowercase all letters</td>
    <td class="caution-bg font-small">str_lower(s)</td>
    <td class="success-bg font-small">s.lower(s)</td>
</tr>
<tr>
    <td class="info-bg font-small">Trim whitespace</td>
    <td class="caution-bg font-small">str_trim(s)</td>
    <td class="success-bg font-small">s.strip(s)</td>
</tr>
<tr>
    <td class="info-bg font-small">Split string into words</td>
    <td class="caution-bg font-small">str_split(s, delim)</td>
    <td class="success-bg font-small">s.split(delim)</td>
</tr>
<tr>
    <td class="info-bg font-small">Join array of strings</td>
    <td class="caution-bg font-small">str_join(sv, delim)</td>
    <td class="success-bg font-small">delim.join(sv)</td>
</tr>
</tbody>
</table>

[string]: https://docs.python.org/3/library/stdtypes.html#str

---

# Data Structures: <span class="gold">Strings</span> (<span class="muted">*Examples*</span>)

<div class="columns">

<div>

```python
# Create string
>>> s = 'Shake it off'

# Get length of string
>>> len(s)
12

# Get first character
>>> s[0]
'S'

# Convert to lowercase
>>> s.lower()
'shake it off'

```

</div>

<div>

```python
# Trim whitespace
>>> '  Shake it off  '.strip()
'Shake it off'

# Split string (by space)
>>> s.split()
['Shake', 'it', 'off']

# Join split string with ,
>>> ','.join(s.split())
'Shake,it,off'

# Slice a string
>>> s[:5]
'Shake'
```

</div>

</div>

---

# Data Structures: <span class="gold">Sets</span>

To create a <strong class="warning">collection</strong> of <strong
class="special">unique values</strong>, we can use a [set], which is
implemented as a <strong class="primary">hash table</strong>:

<table class="bordered">
<thead>
    <th class="info-bg">Operation</th>
    <th class="caution-bg">C</th>
    <th class="success-bg">Python</th>
</thead>
<tbody>
<tr>
    <td class="info-bg font-small">Create empty set</td>
    <td class="caution-bg font-small">Table *t = table_create()</td>
    <td class="success-bg font-small">s = set()</td>
</tr>
<tr>
    <td class="info-bg font-small">Add value to set</td>
    <td class="caution-bg font-small">table_insert(t, value)</td>
    <td class="success-bg font-small">s.add(value)</td>
</tr>
<tr>
    <td class="info-bg font-small">Remove value from set</td>
    <td class="caution-bg font-small">table_remove(t, value)</td>
    <td class="success-bg font-small">s.remove(value)</td>
</tr>
<tr>
    <td class="info-bg font-small">Search set for value</td>
    <td class="caution-bg font-small">table_search(t, value)</td>
    <td class="success-bg font-small">value in s</td>
</tr>
</tbody>
</table>

[set]: https://docs.python.org/3/library/stdtypes.html#set

---

# Data Structures: <span class="gold">Sets</span> (<span class="muted">*Examples*</span>)

```python
>>> s = {0, 1, 2}               # Create set
>>> 3 in s                      # Check if 3 is in set
False

>>> s.add(3)                    # Add 3 to set
>>> 3 in s                      # Check if 3 is in set
True

>>> s.remove(3)                 # Remove 3 from set
>>> 3 in s                      # Check if 3 is in set
False
```

---

# Data Structures: <span class="gold">Dicts</span>

To create a <strong class="danger">collection</strong> of <strong
class="special">key, value pairs</strong>, we can use a [dict], which is
implemented as a <strong class="primary">hash table</strong>:

<table class="bordered">
<thead>
    <th class="info-bg">Operation</th>
    <th class="caution-bg">C</th>
    <th class="success-bg">Python</th>
</thead>
<tbody>
<tr>
    <td class="info-bg font-small">Create empty map</td>
    <td class="caution-bg font-small">Map *m = map_create()</td>
    <td class="success-bg font-small">m = {}</td>
</tr>
<tr>
    <td class="info-bg font-small">Insert key, value pair</td>
    <td class="caution-bg font-small">map_insert(m, key, value)</td>
    <td class="success-bg font-small">m[key] = value</td>
</tr>
<tr>
    <td class="info-bg font-small">Remove key, value pair</td>
    <td class="caution-bg font-small">map_remove(m, key)</td>
    <td class="success-bg font-small">m.pop(key)</td>
</tr>
<tr>
    <td class="info-bg font-small">Lookup value with key</td>
    <td class="caution-bg font-small">map_lookup(m, key)</td>
    <td class="success-bg font-small">m[key] or m.get(key)</td>
</tr>
<tr>
    <td class="info-bg font-small">Search with key</td>
    <td class="caution-bg font-small">map_search(m, key)</td>
    <td class="success-bg font-small">key in m</td>
</tr>
</tbody>
</table>

[dict]: https://docs.python.org/3/library/stdtypes.html#dict

---

# Data Structures: <span class="gold">Dicts</span> (<span class="muted">*Examples*</span>)

<div class="columns">

<div>

```python
# Create dict
>>> d = {'taylor': 9, 'olivia': 5}

# List keys
>>> d.keys()
dict_keys(['taylor', 'olivia'])

# List values
>>> d.values()
dict_values([9, 5])

# List key, value pairs
>>> d.items()
dict_items([('taylor', 9), ('olivia', 5)])

# Lookup value
>>> d['taylor']
9
```

</div>

<div>

```python
# Lookup value with default
>>> d.get('chief', 0)
0

# Add key and value
>>> d['justin'] = 1

# Search dict
>>> 'justin' in d
True

# Remove by key
>>> d.pop('justin')
1

>>> d
{'taylor': 9, 'olivia': 5}
```

</div>

</div>

---

<!-- _class: lead -->

# Command Line Arguments

---

# Arguments: [sys.argv]

To read <strong class="primary">command line arguments</strong>, we need to
<strong class="caution">import</strong> the [sys] module access the [argv]
[list]:

```python
import sys                      # Load sys module

for argument in sys.argv[1:]:   # Loop through each command line argument
    print(argument)
```

<br>

<div class="alert info-bg centered">

**Note**: `sys.argv[0]` is normally the name of the program being executed
(<i>ie. the name of the script</i>).

</div>

[sys]: https://docs.python.org/3/library/sys.html
[argv]: https://docs.python.org/3/library/sys.html#sys.argv
[sys.argv]: https://docs.python.org/3/library/sys.html#sys.argv

---

# Example: [sumup.py]

> Write a program that **sums up** all the integer <strong
> class="primary">command line arguments</strong>:

<div class="columns">

<div>

```python
import sys

numbers = []
for argument in sys.argv[1:]:
    try:
        numbers.append(int(argument))
    except ValueError:
        continue

print(sum(numbers))
```

</div>

<div>

```bash
# Run script with arguments
$ ./sumup.py 1 two 3 four
4
```

</div>

</div>

[sumup.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides05/sumup.py

---

# Arguments: [flags.py]

We can use a <strong class="caution">while</strong> loop to parse <strong
class="primary">command line arguments</strong>:

```python
# Command line arguments and field parameter
arguments = sys.argv[1:]
field     = 0

# Parse arguments as long as non-empty and first argument begins with '-'
while arguments and arguments[0].startswith('-'):
    match argument := arguments.pop(0):             # Walrus: assign and check
        case '-f': field = int(arguments.pop(0))    # Handle -f FIELD flag
        case '-h': usage(0)                         # Handle -h flag
        case _:    usage(1)                         # Handle unknown flag

print(f'{field=}')
```

[flags.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides05/flags.py

---

<!-- _class: lead -->

# I/O

---

# I/O: [sys.stdin]

To process <strong class="danger">standard input</strong> line by line, we can loop over
[sys.stdin]:

<div class="columns">

<div>

```python
import sys

# Loop over stdin line by line
for line in sys.stdin:
    line = line.rstrip()
    print(line)
```

</div>

<div>

```python
import sys

# Loop over stdin line by line
while line := sys.stdin.readline():
    line = line.rstrip()
    print(line)
```

</div>

</div>

<br>

<div class="alert info-bg centered">

**Note**: the [str.rstrip] is necessary because `line` will contain a `\n` (ie.
*newline*) at the end of the [string].

</div>

[sys.stdin]: https://docs.python.org/3/library/sys.html#sys.stdin
[str.rstrip]: https://docs.python.org/3/library/stdtypes.html#str.rstrip

---

# I/O: [input]

To interactively prompt the user, we can use the [input] function:

```python
# Prompt user for name and greet them
name = input('What is your name? ')
print(f'Hello, {name}!')
```

[input]: https://docs.python.org/3/library/functions.html#input

---

# Example: [leetspeak.py]

> Write a [leetspeak] translator.

<div class="columns">

<div>

```python
def main(arguments: list[str]=sys.argv[1:]):
    fr_chars = 'aeio'
    to_chars = '4310'

    while arguments and arguments[0].startswith('-'):
        match argument := arguments.pop(0):
            case '-f': fr_chars = arguments.pop(0)
            case '-t': to_chars = arguments.pop(0)
            case '-h': usage(0)
            case _   : usage(1)

    mapping = {}
    for fr, to in zip(fr_chars, to_chars):
        mapping[fr] = to

    for line in sys.stdin:
        print(leetspeak(line, mapping), end='')
```

</div>

<div>

```python
def leetspeak(text: str, mapping: dict[str, str]) -> str:
    ''' Translate each line of text into leetspeak '''
    result = []
    for letter in text:
        result.append(mapping.get(letter.lower(), letter))
    return ''.join(result)
```

```bash
# Run with default mapping
$ echo we are the tide | ./leetspeak.py
w3 4r3 th3 t1d3

# Run with custom mapping
$ echo we are the tide | ./leetspeak.py -f et -t 37
w3 ar3 7h3 7id3
```

</div>

</div>

[leetspeak]: https://en.wikipedia.org/wiki/Leet
[leetspeak.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides05/leetspeak.py

---

# I/O: <span class="gold">Reading Files</span>

To process the data in a <strong class="primary">file</strong> line by line, we
can loop over an [open] <strong class="primary">file object</strong>:

```python
# Loop through file at path line by line
for line in open(path):
    line = line.rstrip()
    print(line)
```

[open]: https://docs.python.org/3/library/functions.html#open

---

# I/O: <span class="gold">Writing Files</span>

To store data into <strong class="primary">file</strong>, we can use the [open]
function with the [with] <strong class="success">context manager</strong>:

```python
# Open file at path for writing and then write data to it
with open(path, 'w') as fs:
    fs.write(data)
```

The purpose of the [with] <strong class="success">context manager</strong> is
that it will automatically <strong class="danger">close</strong> the <strong
class="primary">file</strong> for us when we leave its scope.

[with]: https://docs.python.org/3/reference/compound_stmts.html#with

---

# Example: [anagram.py]

> Given two words, determine if they are [anagrams].

```bash
$ ./anagram.py -i       # Ignore case
listen silent
ANAGRAM!
army Mary
ANAGRAM!
card dare
NOT ANAGRAM!
```

[anagrams]: https://en.wikipedia.org/wiki/Anagram
[anagram.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides05/anagram.py
