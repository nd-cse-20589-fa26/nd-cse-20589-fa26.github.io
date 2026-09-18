---
title: "Slides 10: Networking"
description: "Networking"
author: Peter Bui
keywords: lecture,sos,networking
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides10.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Networking

---

# Networking: <span class="gold">Motivating Questions</span>

<div class="font-large">

1. What is my <strong class="caution">IP address</strong>?

2. What is Notre Dame's <strong class="caution">IP address</strong>?

3. What <strong class="success">services</strong> are running on my machine?

4. What <strong class="success">services</strong> are running on your machine?

5. How do I retrieve something from the <strong class="danger">web</strong>?

6. How do we measure <strong class="info">bandwidth</strong> and <strong
   class="info">latency</strong>?

7. How do I <strong class="warning">transfer</strong> files between machines?

</div>

---

# Networking: <span class="gold">Overview</span>

<strong class="primary">Networking</strong> involves connecting computers so
they can talk to each other!

<img src="https://thumb.wikimedia.org/wikipedia/commons/thumb/5/5e/NetworkDecentral.svg/960px-NetworkDecentral.svg.png" class="float-right" width="500px">

<br>

### <strong class="danger">Challenges</strong>

- Protocols
- Security
- Speed
- Reliability

---

# Networking: <span class="gold">The Internet</span>

<strong class="caution">Loose, unstructured, chaotic, ad hoc collection of
networks</strong>, bound together by <strong
class="warning">standards</strong>.

<img src="https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d2/Internet_map_1024.jpg/500px-Internet_map_1024.jpg" class="float-right">

- Designed to tolerate failures.

- Network of networks.

- It is more than just the web!

---

# Networking: <span class="gold">OSI Model</span>

<div class="centered">

<img src="https://o.quizlet.com/cwPOIxf4a3Uwpc9cMllQiQ_b.jpg">

</div>

---

# Networking: <span class="gold">Network Layer</span>

Handles routing among nodes by grouping data into <strong
class="success">packets</strong>.

<img src="https://images.ctfassets.net/slt3lc6tev37/5biqo5wm6nM8GSmiNyiAnl/b6b5c9befeda6ba99b4380d84953de18/routing-diagram.svg" width="675px" class="float-right">

- IPv4, IPv6
- Routing

#### <strong class="caution">Router</strong>

Connects two different networks.

<br>

#### <strong class="caution">Gateway</strong>

Similar to router, except in that it also translates between one network system
or protocol and another.

---

# Networking: <span class="gold">Transport Layer</span>

Implements a process-to-process channel for exchanging <strong
class="caution">messages</strong>.

- UDP
- TCP

<img src="https://www.differencebetween.info/sites/default/files/images/2/ip.jpg" class="framed float-right" width="400px">

#### <strong class="caution">Transmission Control Protocol</strong>

Provides a reliable two-way stream.

<br>

#### <strong class="caution">IP</strong>

Provides unreliable connectionless packet delivery.

---

# Networking: <span class="gold">IP Address</span>

> What is my <strong class="caution">IP Address</strong>?

<div class="columns-1-2">

<div>

```bash
# Old Method
$ ifconfig

# New Method
$ ip addr
```

</div>

<div>

- Most machines will have more than one <strong class="caution">IP Address</strong>.

- Almost every machine will have the `127.0.0.1` <strong class="caution">IP
  Address</strong> (aka. <i class="warning">localhost</i>).

- Some <strong class="caution">IP Addresses</strong> are **public** (ie.
  reachable from anyone on the Internet), while others are **private** (ie.
  only reachable from the local network).

</div>

</div>

---

# Networking: <span class="gold">DNS</span>

> What is Notre Dame's <strong class="caution">IP Address</strong>?

<div class="columns-1-2">

<div>

```bash
# Using dig
$ dig nd.edu

# Using host
$ host nd.edu

# Using nslookup
$ nslookup nd.edu
```

</div>

<div>

<div class="centered">

<div class="font-small"><br></div>

<img src="https://images.ctfassets.net/slt3lc6tev37/3NOmAzkfPG8FTA8zLc7Li8/8efda230b212c0de2d3bbcb408507b1e/dns_record_request_sequence_recursive_resolver.png" width="775px" class="framed">

</div>

```python
# Using gethostbyname in Python
>>> socket.gethostbyname('nd.edu')
```

</div>

</div>

---

# Networking: <span class="gold">Services/Ports</span>

> What <strong class="sucess">services/ports</strong> are running on my machine?

<div class="columns-2-1">

<div>

```bash
# Old Method
$ netstat -tulnp

# New Method
$ ss -tulnp
```

</div>

<div>

<table class="bordered">
<thead>
    <th class="info-bg">Service</th>
    <th class="success-bg">Port</th>
</thead>
<tbody>
<tr>
    <td class="info-bg">SSH</td>
    <td class="success-bg">22</td>
</tr>
<tr>
    <td class="info-bg">HTTP</td>
    <td class="success-bg">80</td>
</tr>
<tr>
    <td class="info-bg">HTTPS</td>
    <td class="success-bg">443</td>
</tr>
</tbody>
</table>

</div>

</div>

<br>

<div class="alert warning-bg">

On the **student machiness**, ports `9000`-`9999` are open to other machines on
the <strong class="primary">Notre Dame</strong> network.

</div>

---

# Networking: <span class="gold">Port Scanning</span>

> What <strong class="success">services</strong> are running on your machine?

Even though certain <strong class="success">services</strong> are associated
with particular <strong class="success">ports</strong>, applications may listen
on any <strong class="success">port</strong>.

To see what ports are open on another machine, you can use [nmap]:

```bash
# Scan remote machine for open ports
$ nmap -v -Pn host
```

<br>

<div class="alert danger-bg centered">

System and Network Administrators may frown upon this...

</div>

[nmap]: https://nmap.org/

---

# Networking: <span class="gold">Client/Server</span>

<div class="centered margin-top-0-5">

<img src="static/img/notes09-requests-http.svg" width="750px">

</div>

<div class="columns">

<div>

<strong class="info">Clients</strong> (ie. *web browser*) makes a <strong
class="success">request</strong> for a document or resource.

</div>

<div>

<strong class="danger">Servers</strong> (ie. *web application*) receives
<strong class="success">request</strong>, processes it, and sends back
<strong class="danger">response</strong>

</div>

</div>

---

# Networking: <span class="gold">HTTP</span>

> How do I retrieve something from the <strong class="danger">web</strong>?

<div class="columns">

<div>

```bash
# Dump to standard output
$ curl http://www.google.com

# Download file
$ wget http://www.google.com
```

</div>

<div>

```bash
# Manually with netcat
$ nc www.google.com 80
GET / HTTP/1.0
Host: www.google.com
...
```

</div>

</div>

---

# Networking: <span class="gold">HTTP</span> (<i class="muted">Python</i>)

```python
# Client: download using requests in Python
>>> import requests
>>> response = requests.get('https://www.google.com')
>>> response.text
```

<br>

```bash
# Server: share files in current directory over HTTP 
# using Python on port 9999
$ python3 -m http.server 9999
Serving HTTP on 0.0.0.0 port 9999 (http://0.0.0.0:9999/) ...
```

---

# Networking: <span class="gold">Bandwidth, Latency</span>

> How do we measure <strong class="info">bandwidth</strong> (<i
> class="muted">capacity</i>) and <strong
   class="info">latency</strong> (<i class="muted">delay</i>)?

```bash
# Bandwidth: Download linux kernel
$ wget https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-6.18.4.tar.xz

# Latency: Ping cdn.kernel.org
$ ping cdn.kernel.org

# Latency: Trace networking route
$ traceroute nd.edu
```

---

# Networking: <span class="gold">SSH</span>

<div class="columns margin-top-0-5">

<div>

### <strong class="warning">Remote Shell</strong>

```bash
# Login to another machine
$ ssh student10.cse.nd.edu

# Execute remote command
$ ssh remote.host uname -a

# Execute remote command
$ cat file | ssh remote.host tee file
```

</div>

<div>

### <strong class="warning">File Transfer</strong>

```bash
# Copy file to another machine
$ scp file remote:~/file


# Interactively transfer files
$ sftp student10.cse.nd.edu
sftp> cd /tmp
sftp> put upload
sftp> get download


# Synchronize files
$ rsync -av --progress folder remote:path
```

</div>

</div>

