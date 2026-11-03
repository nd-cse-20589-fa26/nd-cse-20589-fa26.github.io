---
title: "Notebook 25: HTTP"
description: "HTTP"
author: Peter Bui
keywords: notebook,sos,system calls,networking,http
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/notebook25.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## HTTP

---

# Review: [echo_client] / [echo_server]

<div class="columns">

<div class="centered margin-top-0-5">

## <span class="info">Client</span>

<br>

<img src="static/img/slides24-client-blank.svg">

</div>

<div class="centered margin-top-0-5">

## <span class="danger">Server</span>

<br>

<img src="static/img/slides24-server-blank.svg">

</div>

</div>

[echo_client]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides24/echo_client.py
[echo_server]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides24/echo_server.py

---

# Review: <span class="gold">URL</span>

<div class="slide-centered">

<img src="static/img/slides24-url-blank.svg">

</div>

---

# HTTP: <span class="gold">Overview</span>

<strong class="special">HTTP</strong>
(<strong class="special">__________________________</strong>) is a communication protocol where:

<br>

<div class="centered">

<img src="static/img/notes09-requests-http.svg">

</div>

1. <strong class="info"> ______________</strong> (*ie. `_________`*) makes
   <strong class="caution">request</strong> for resource.

2. <strong class="danger"> ______________</strong> (*ie. `_________`*) returns
   <strong class="warning">response</strong> with resource.

---

# HTTP: <span class="gold">Client</span>

<div class="slide-centered">

<img src="static/img/slides25-http-client-blank.svg">

</div>

---

# HTTP: <span class="gold">Server</span>

<div class="slide-centered">

<img src="static/img/slides25-http-server-blank.svg">

</div>
