---
title: "Slides 04: Python, Control Flow, Modules"
description: "Files, Processes, I/O"
author: Peter Bui
keywords: lecture,sos,python,control flow,modules
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides04.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Python, Control Flow, Modules

---

<!-- _class: lead -->

# Python

---

# Python: <strong class="gold">Overview</strong>

Python is an <strong class="caution">interpreted</strong>, <strong
class="warning">object-oriented</strong>, <strong
class="success">high-level</strong> **programming language** with dynamic
semantics.

<div class="columns">

<div class="font-smaller">

- Encourages very <strong class="info">readable</strong> and <strong
  class="info">well structured</strong> code.

- Rich <strong class="caution">ecosystem of libraries</strong> and <strong
  class="caution">frameworks</strong> ([NumPy], [Pandas], [Django], [Flask],
  [TensorFlow], [PyTorch], etc.).

- <strong class="success">Free</strong> and <strong class="success">open
  source</strong>, widely spread, with vibrant <strong
  class="special">community</strong>.

[NumPy]: https://numpy.org/
[Pandas]: https://pandas.pydata.org/
[Django]: https://www.djangoproject.com/
[Flask]: https://flask.palletsprojects.com/en/stable/
[TensorFlow]: https://www.tensorflow.org/
[PyTorch]: https://pytorch.org/

</div>

<div class="centered middled">

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/500px-Python_logo_and_wordmark.svg.png">

</div>

</div>

---

# Python: <strong class="gold">Industry Adoption</strong>

<br>

<div class="slide-centered">

<img src="static/img/slides04-python-industry-adoption.png" height="550px">

</div>

---

# Python: <strong class="gold">Antigravity</strong>

<br>

<div class="slide-centered">

<a href="https://xkcd.com/353/">
<img src="https://imgs.xkcd.com/comics/python.png" height="525px" class="framed">
</a>

</div>

---

<!-- _class: lead -->

# Scripting

---

# Scripting: <strong class="gold">Intepreter</strong>

As with <strong class="primary">bash</strong>, <strong
class="success">Python</strong> is an <strong
class="caution">intepreted</strong> programming language:

```python
$ python3
Python 3.12.4 (main, Aug  6 2024, 12:19:55) [GCC 8.5.0 20210514 (Red Hat 8.5.0-10)] on linux
>>> print('Hello, World!')
Hello, World!
```

<br>

<div class="alert success-bg">

<div class="centered">

On the `student machines`, to ensure you have <strong class="success">Python
3.12</strong>, you will want to add the following to your `~/.bashrc`:

</div>

```bash
export PATH=~pbui/pub/pkgsrc/bin:$PATH
```

</div>

---

# Scripting: <strong class="gold">Scripts</strong>

<div class="columns">

<div>

To create a <strong class="success">Python</strong>, we need a <strong
class="hljs-comment">shebang</strong> and to make the script <strong
class="caution">executable</strong>.

</div>

<div>

```python
# Create hello.py script
$ cat > hello.py <<EOF
#!/usr/bin/env python3
print('Hello, World!')
EOF

# Make script executable
$ chmod +x hello.py

# Run script
$ ./hello.py
Hello, World!
```

</div>

</div>

---

# Scripting: <strong class="gold">Comments</strong>

To comment code in <strong class="success">Python</strong>, we can use <strong
class="hljs-comment">#</strong> just as in <strong
class="primary">bash</strong>, or we can just create <strong
class="danger">strings</strong>:

```python
# Comment
print("I'm not dead yet!")

# Docstring
''' Ignore this block of code
print('What have the Romans ever done for us?')
'''
```

---

<!-- _class: lead -->

# Variables, Types, Expressions

---

# VTE: <strong class="gold">Objects</strong>

<div class="columns">

<div>

Everything in <strong class="success">Python</strong> is an <strong class="primary">object</strong>:

- Has a <strong class="caution">type</strong>

- Has <strong class="special">methods</strong> (*functions*)

- Has <strong class="special">attributes</strong> (*data*)

</div>

<div>

```python
# Get type of object
>>> type('Python')
<class 'str'>

# List attributes of object
>>> dir('Python')
['__add__', '__class__',
...
'strip', 'swapcase', 'title',
'translate', 'upper', 'zfill']

# Call upper method of string object
>>> 'Python'.upper()
'PYTHON'
```

</div>

</div>

---

# VTE: <strong class="gold">Variables, Types</strong>

<div class="columns-1-1-1">

<div>

<strong class="caution">Variables</strong> are assigned in the following
format:

<div class="centered">

**name** = **value**

</div>

<div class="font-smaller">

- Although we don't specify a <strong class="caution">type</strong> during
  assignment, every <strong class="primary">object</strong> in <strong
  class="success">Python</strong> has a <strong class="caution">type</strong>.

- We can <strong class="special">convert</strong> between different <strong
  class="caution">types</strong>.

</div>

</div>

<div>

```python
# Define string variable
>>> name = 'Python'

# Get type of variable
>>> type(name)
<class 'str'>

# Print variable
>>> print(name)
Python

# Convert string to list
>>> list(name)
['P', 'y', 't',
 'h', 'o', 'n']
```

</div>

<div>

```python
# Define float variable
>>> number = 3.14

# Get type of variable
>>> type(number)
<class 'float'>

# Display variable
>>> number
3.14

# Convert float to int
>>> int(number)
3
```

</div>

</div>

---

# VTE: <strong class="gold">Expressions</strong>

<div class="columns-1-2">

<div>

<strong class="success">Python</strong> supports a variety of <strong
class="primary">arithmetic</strong> and <strong class="danger">boolean</strong>
expressions.

<div class="font-smaller">

- [Arithmetic Operators and Expressions](https://realpython.com/python-operators-expressions/#arithmetic-operators-and-expressions-in-python) in <strong class="success">Python</strong>

- [Boolean Operators and Expressions](https://realpython.com/python-operators-expressions/#boolean-operators-and-expressions-in-python) in <strong class="success">Python</strong>

</div>

</div>

<div>

```python
# Arithmetic
>>> 2 + 4 * 3 / 2
8.0
>>> 2 + 4 * 3 // 2  # Integer division
8

# Modulus and Logical comparisons
>>> (7 % 2) or (8 % 2)
1
>>> (7 % 2) and (8 % 2)
0

# String comparison
>>> 'python' > 'bash'
True
```

</div>

---

<!-- _class: lead -->

# Control Flow

---

# Control Flow: <strong class="gold">Conditional</strong>

We can <strong class="special">conditionally</strong> execute different blocks
of code with the <strong class="caution">if</strong> statement:

```python
number = random.randint(0, 10)

if number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print(number)
```

---

# Control Flow: <strong class="gold">Exceptions</strong>

<strong class="danger">Errors</strong> can be signaled to the program via
<strong class="danger">exceptions</strong>, which can be programmatically
caught and handled:

```python
# Declare list of numbers
numbers = [0, 1, 2, 3]

try:
    print(numbers[4])   # Error: Out of bounds access!!!
except IndexError as e: # Catch: Handle exception
    print('Oops!', e)
```

---

# Control Flow: <strong class="gold">Loops</strong>

We can perform <strong class="special">repeated execution</strong> by using
<strong class="caution">for</strong> or <strong class="caution">while</strong>
loops:

<div class="columns">

<div>

```python
# Loop through list of numbers
for number in [0, 1, 2]:
    print (number)
```

</div>

<div>

```python
index   = 0
numbers = [0, 1, 2]

# Loop through list of numbers
while index < len(data):
    print(data[index])
    index += 1
```
</div>

</div>

---

# Control Flow: <strong class="gold">Range, Enumerate</strong>

We can generate a **sequence** of numbers using <strong
class="primary">range</strong>, and a **sequence** of index, value pairs using
<strong class="primary">enumerate</strong>:

```python
# Print 2, 3, 4
for value in range(2, 5):
    print(value)

# Print 2, 3, 4 with indices
for index, value in enumerate(range(2, 5)):
    print(index, value)
```

---

# Example: [Rolling Dice](https://github.com/nd-cse-20589-fa26/examples/blob/master/slides04/roll.py)

> Simulate **rolling dice** until you hit [snake eyes] (🎲🎲).

[snake eyes]: https://en.wikipedia.org/wiki/Dice#Etymology_and_terms

```python
die1, die2 = random.randint(1, 6), random.randint(1, 6) # Destructuring assignment

while (die1 + die2) != 2:
    if die1 == 1 or die2 == 1:
        print(f'! Bruh: {die1}, {die2}')                # Format-string
    else:
        print(f'- Nope: {die1}, {die2}')

    die1, die2 = random.randint(1, 6), random.randint(1, 6)

print(f'+ Yeah: {die1}, {die2}')
```

---

<!-- _class: lead -->

# Functions

---

# Functions: <strong class="gold">Declaration</strong>

We can group blocks of code into <strong class="caution">functions</strong>:

```python
>>> def increment(n, amount=1):     # Keyword argument
        ''' Returns n + amount '''  # Docstring
        return n + amount

>>> print(increment(1))             # n is 1, amount is 1
2
>>> print(increment(1, 2))          # n is 1, amount is 2
3
>>> print(increment(1, amount=4))   # n is 1, amount is 4
5
```

---

# Functions: <strong class="gold">Keyword Arguments</strong>

<div class="columns">

<div>

<strong class="caution">Function</strong> **arguments** can be specified by
their <strong class="special">keyword</strong>.

```python
def repeat(s, n=5):
    for _ in range(n):
        print(s)
```

<strong class="special">Keyword</strong> **arguments** also serve as
**defaults** if the caller does not specify a parameter.

</div>

<div>

```python
# Repeat hi 5 times
repeat('hi')

# Repeat hi 4 times
repeat('hi', 4)

# Repeat hi 7 times
repeat('hi', n=7)
```

</div>

</div>

---

# Functions: <strong class="gold">Scope</strong>

<strong class="success">Python</strong> has **local scoping** rules:

```python
>>> x = 0                   # Global x
>>> def increment(x):
        x = x + 1           # Local x
        return x

>>> print(x)
0
>>> print(increment(x))
1
>>> print(x)
0
```

---

<!-- _class: lead -->

# Documentation

---

# Documentation: <strong class="gold">Docstrings</strong>

<strong class="caution">Functions</strong> may include a <strong
class="danger">docstring</strong> under their declaration to describe their
arguments and behavior.

```python
>>> def repeat(s, n=5):     # Define function
        ''' Print s out n times '''
        for _ in range(n):
            print(s)

>>> help(repeat)            # View docstring of function
...
repeat(s, n=5)
    Print s out n times
```

---

# Documentation: <strong class="gold">Doctests</strong>

<strong class="caution">Function</strong> <strong
class="danger">docstrings</strong> can be extended to include usage examples
what serve as <strong class="warning">unit tests</strong>:

<div class="columns">

<div>

```python
# script.py
def increment(n, amount=1):
    ''' Returns n + amount

    >>> increment(1)
    2
    >>> increment(1, 4)
    5
    '''
    return n + amount
```

</div>

<div>

```bash
# Run doctests
$ python3 -m doctest script.py

# Run doctests with verbose output
$ python3 -m doctest -v script.py

# Run doctest for specific function
$ doctestfn script.py increment

```

</div>

</div>

---

# Documentation: <strong class="gold">Type Annotations</strong>

In <strong class="success">Python</strong>, we can provide (*optional*) [type
annotations] to describe the <strong class="caution">types</strong> of <strong
class="caution">functions</strong> and <strong
class="caution">variables</strong>.

```python
def increment(n: int, amount: int=1) -> int:
    return n + amount

increment(0)        # OK
increment('s')      # MyPy will find type error
```

<br>

<div class="alert warning-bg centered">

The <strong class="success">Python</strong> interpreter <strong
class="danger">will not check type annotations</strong>.  Instead, you must use
a third party tool such as [mypy] to check for errors.

</div>

[type annotations]: https://docs.python.org/3/library/typing.html
[mypy]: https://mypy-lang.org/

---

<!-- _class: lead -->

# Modules

---

# Module: <strong class="gold">Imports</strong>

To use <strong class="caution">functions</strong> and <strong
class="primary">objects</strong> from other <strong
class="success">Python</strong> scripts, we use the <strong
class="caution">import</strong> command to load the external <strong
class="special">modules</strong>.

<div class="columns">

<div>

```python
# Load random module
>>> import random

# Use function from random module
>>> random.randint(1, 6)
3
```

</div>

<div>

```python
# Load specific function from
# random module
>>> from random import randint

# Use function from random module
>>> randint(1, 6)
4
```

</div>

</div>

---

# Module: <strong class="gold">Import Guard</strong>

To separate what should be executed when a <strong
class="success">Python</strong> script is loaded as a <strong
class="special">module</strong> versus when it is run as a <strong
class="primary">program</strong>, use the <strong
class="danger">__name__</strong> **import guard** pattern:

```python
# Main function
def main():
     ...

# Check if script is being executed as a program
if __name__ == '__main__':
    main() # Only executed when run as a program
```

---

# Example: [Fizz Buzz](https://github.com/nd-cse-20589-fa26/examples/blob/master/slides04/fizzbuzz.py)

> Write a program that prints the numbers from `1` to `100`. But for multiples
> of **three** print <strong class="danger">"Fizz"</strong> instead of the
> number and for the multiples of **five** print <strong
> class="danger">"Buzz"</strong>. For numbers which are multiples of both
> **three** and **five** print <strong class="danger">"FizzBuzz"</strong>.

<br>

<div class="centered">

<img src="https://storage.ghost.io/c/eb/aa/ebaa2665-01a8-4415-8825-69d1f0e8fd19/content/images/size/w320/2025/01/coding-horror-logo-transparency.png" height="200px">

[Why Can't Programmers... Program?](https://blog.codinghorror.com/why-cant-programmers-program/) -- [Jeff Atwood](https://en.wikipedia.org/wiki/Jeff_Atwood)

</div>

