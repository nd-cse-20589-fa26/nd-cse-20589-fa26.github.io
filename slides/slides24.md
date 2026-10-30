---
title: "Slides 24: Sockets"
description: "Sockets"
author: Peter Bui
keywords: lecture,sos,system calls,networking,sockets
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides24.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Sockets

---

# Review: <span class="gold">Looking Back, Moving Forward</span>

<div class="font-large">

1. What is <strong class="primary">networking</strong>?

    - What is an <strong class="caution">IP address</strong>?

    - What is a <strong class="warning">port</strong>?

    - What is a <strong class="info">domain name</strong>?

    - What is a <strong class="success">URL</strong>?

2. What is a <strong class="special">protocol</strong>?

</div>

---

# Review: <span class="gold">Networking Terms</span>

<strong class="caution">IP address</strong>

Unique number for identifying machine.

<strong class="warning">port</strong>

Unique number for identifying a service on a machine.

<strong class="info">domain name</strong>

A string that maps to one or more IP addresses.

<strong class="special">protocol</strong>

Rules for exchanging communication.

---

# Review: <span class="gold">URL</span>

A <strong class="success">URL</strong> is a <strong class="success">uniform
resource locator</strong> that corresponds to a resource on the Internet:

<br>
<br>

<div class="centered">

<img src="static/img/slides24-url.svg">

</div>

---

# Review: <span class="gold">Transport</span>

<div class="columns">

<div class="margin-top-0-5">

## <span class="success">TCP</span>

Provides a <strong class="success">reliable</strong> two-way stream.

</div>

<div class="margin-top-0-5">

## <span class="danger">UDP</span>

Provides a <strong class="danger">unreliable</strong> connectionless packet delivery.

</div>

</div>

<br>

<div class="centered">

<img src="static/img/slides24-transport.svg">

</div>

---

# Sockets: <span class="gold">Overview</span>

A <strong class="success">socket</strong> is a special <strong class="caution">file descriptor</strong>
that corresponds to a network endpoint:

<table class="bordered">
<thead>
    <th class="info-bg">Regular File</th>
    <th class="info-bg">Socket</th>
</thead>
<tbody>
<tr class="success-bg">
    <td>open</td>
    <td>socket / connect, socket / bind / listen / accept</td>
</tr>
<tr class="caution-bg">
    <td>read</td>
    <td>recv</td>
</tr>
<tr class="caution-bg">
    <td>write</td>
    <td>send</td>
</tr>
<tr class="danger-bg">
    <td>close</td>
    <td>close / shutdown</td>
</tr>
</tbody>
</table>

When using <strong class="success">TCP sockets</strong>, we can convert the
<strong class="caution">file descriptor</strong> into a <strong
class="warning">stream</strong> with the normal read and write methods!

---

# Sockets: <span class="gold">Client / Server</span>

<div class="columns">

<div class="margin-top-0-5">

## <span class="info">Client</span>

Program that *dials* into another program and makes a request.

<br>

<div class="centered">

<img src="static/img/slides24-client.svg">

</div>

</div>

<div class="margin-top-0-5">

## <span class="danger">Server</span>

Program that *wait* for connections and *handles* them.

<br>

<div class="centered">

<img src="static/img/slides24-server.svg">

</div>

</div>

</div>

---

# Sockets: <span class="gold">Making a Connection</span>

To make a connection, a <strong class="info">client</strong> must do the following:

```python
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client: # 1. Create a TCP Socket
    client.connect((host, port))    # 2. Connect TCP Socket to host and port
    ...
```

<div class="font-smaller">

- [socket.socket] creates a special <strong class="success">file-like</strong> object we can
  use to communicate over the network.

- The [socket.AF_INET] means we want to use **IPv4** and [socket.SOCK_STREAM]
  means we want to use <strong class="success">TCP</strong>.

- [socket.connect] establishes a <strong class="success">TCP</strong> connect between the
  <strong class="info">client</strong> and <strong class="danger">server</strong>.

- Once connected, we can use [socket.send] to write a request to the
  <strong class="danger">server</strong> and [socket.recv] to read a response.

</div>

[socket.socket]: https://docs.python.org/3/library/socket.html#socket.socket
[socket.AF_INET]: https://docs.python.org/3/library/socket.html#socket.AF_INET
[socket.SOCK_STREAM]: https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM
[socket.connect]: https://docs.python.org/3/library/socket.html#socket.socket.connect
[socket.send]: https://docs.python.org/3/library/socket.html#socket.socket.send
[socket.recv]: https://docs.python.org/3/library/socket.html#socket.socket.recv

---

# Sockets: <span class="gold">Handling a Connection</span>

To handle a connection, a <strong class="danger">server</strong> must do the following:

```python
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server: # 1. Create a TCP Socket
    server.bind((host, port))           # 2. Bind to port
    server.listen()                     # 3. Listen on port
    client, address = server.accept()   # 4. Accept a client connection
    ...
```

<div class="font-smaller">

- [socket.bind] tells the <strong class="caution">OS</strong> that the
  <strong class="success">process</strong> expects connections on specified
  <strong class="warning">port</strong>.

- [socket.listen] makes the <strong class="special">socket</strong> available
  for receiving connections.

- [socket.accept] waits and receives an incoming connection from a <strong
  class="info">client</strong>.

</div>

[socket.bind]: https://docs.python.org/3/library/socket.html#socket.socket.bind
[socket.listen]: https://docs.python.org/3/library/socket.html#socket.socket.listen
[socket.accept]: https://docs.python.org/3/library/socket.html#socket.socket.accept

---

# Sockets: <span class="gold">Resolving Hostnames</span>

[socket.connect] and [socket.bind] require <strong class="caution">IP addresses</strong> (ie.
`127.0.0.1`), but users often specify domain names (ie. `nd.edu`).
Fortunately, the [Python] versions of these <strong class="warning">system calls</strong>
will automatically perform this translation for us.

If we want resolve the <strong class="caution">IP address</strong> explicitly, however, we
can use [socket.gethostbyname]:

```python
# Lookup the IP address for nd.edu
>>> socket.gethostbyname('nd.edu')
'34.193.237.201'
```

[socket.bind]: https://docs.python.org/3/library/socket.html#socket.socket.bind
[socket.connect]: https://docs.python.org/3/library/socket.html#socket.socket.connect
[socket.gethostbyname]: https://docs.python.org/3/library/socket.html#socket.gethostbyname
[Python]: https://python.org

---

# Sockets: [echo_client] / [echo_server]

<div class="columns">

<div>

> Write a **echo** <strong class="info">client</strong> that connects to a
> remote machine and sends messages from stdin to the remote machine.

```bash
# Connect to server at port 9999 on localhost
$ ./echo_client.py localhost 9999
Connected to localhost:9999
hello, world
hello, world
```

</div>

<div>

> Write a **echo** <strong class="danger">server</strong> that listens on a
> <strong class="warning">port</strong> and handles a connection by sending
> back any request it receives.

```bash
# Listen for clients at port 9999 on localhost
$ ./echo_server.py 9999
Listening on 127.0.0.1:9999
Accepted connection from 127.0.0.1:51530
hello, world
```

</div>

[echo_client]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides24/echo_client.py
[echo_server]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides24/echo_server1.py
