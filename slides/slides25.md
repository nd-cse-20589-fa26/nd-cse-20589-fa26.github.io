---
title: "Slides 25: HTTP"
description: "HTTP"
author: Peter Bui
keywords: lecture,sos,system calls,networking,http
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides25.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## HTTP

---

# HTTP: <span class="gold">Overview</span>

<strong class="special">HTTP</strong> or <strong class="special">Hypertext
transfer protocol</strong>, is a communication protocol where:

<div class="centered">

<img src="static/img/notes09-requests-http.svg">

</div>

1. A <strong class="info">client</strong> (*ie. `curl`*) makes a <strong
   class="caution">request</strong> for a specific resource.

2. A <strong class="danger">server</strong> (*ie. `nginx`*) returns a <strong
   class="warning">response</strong> to the <strong
   class="info">client</strong> containing the requested information.

---

# HTTP: <span class="gold">Transaction</span>

<div class="columns">

<div class="margin-top-0-5">

## <span class="info">Client</span>

To retrieve a resource, the <strong class="info">client</strong> sends a
<strong class="special">HTTP</strong> <strong class="caution">request</strong>.

```
GET /index.html HTTP/1.0\r\n
Host: www.example.com\r\n
\r\n
```

<div class="font-smaller">

- The first line corresponds to the <strong class="special">HTTP</strong>
  **method** (`GET`).

- The proceeding lines are part of the <strong class="special">HTTP</strong>
  **headers** that describe the <strong class="info">client</strong> or the
  <strong class="caution">request</strong>.

</div>

</div>

<div class="margin-top-0-5">

## <span class="danger">Server</span>

After processing the <strong class="caution">request</strong>, the <strong
class="danger">server</strong> will send back a <strong
class="warning">response</strong>.

```
HTTP/1.0 200 OK\r\n
Content-Type: text/html\r\n
\r\n
<html><body>Hi</body></html>
```

<div class="font-smaller">

- The first line is the <strong class="warning">response</strong> status,
  followed by any **headers**.

- After an empty line follows the <strong class="caution">requested</strong>
  **content**.

</div>

</div>

</div>

---

# HTTP: <span class="gold">Client</span>

<div class="slide-centered">

<img src="static/img/slides25-http-client.svg">

<br>
<br>

## [http_client.py]

</div>

[http_client.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides25/http_client.py

---

# HTTP: <span class="gold">Server</span>

<div class="slide-centered">

<img src="static/img/slides25-http-server.svg">

<br>
<br>

## [http_server.py]

</div>

[http_server.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides25/http_server.py
