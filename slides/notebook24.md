---
title: "Notebook 24: Sockets"
description: "Sockets"
author: Peter Bui
keywords: notebook,sos,system calls,networking,sockets
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/notebook24.html
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

    - What is an **example**?

</div>

---

# Review: <span class="gold">TCP/IP</span>

<div class="slide-centered">

<img src="static/img/slides24-tcpip-blank.svg">

</div>

---

# Review: <span class="gold">URL</span>

<div class="slide-centered">

<img src="static/img/slides24-url-blank.svg">

</div>

---

# Sockets: [echo_client] / [echo_server]

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
