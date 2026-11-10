---
title: "Notebook 27: REST, Vial"
description: "REST, Vial"
author: Peter Bui
keywords: notebook,sos,http,rest,vial
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/notebook27.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## REST, Vial

---

# REST: <span class="gold">Overview</span>

<strong class="special">REST</strong> (<b>___________________________________________</b>) and is a

<strong class="success"> _____________________________________</strong>.

<br>

<div class="columns">

<div>

1. <strong class="success"> ___________________________</strong>:

    <br>

2. <strong class="info">    ___________________________</strong>:

    <br>

3. <strong class="caution"> ___________________________</strong>:

</div>

<div class="centered">

<img src="static/img/software-systems.svg">

</div>

</div>

---

# REST: <span class="gold">HTTP Methods</span>

A <strong class="special"> ________________________</strong> adheres to <strong
class="special">REST</strong> architecture constraints by exposing their data
(ie. <strong class="warning">resources</strong>) to the outside world through
an API accessible via public [HTTP] <strong class="success">URLs</strong>.

<table class="bordered">
<thead>
    <th class="special-bg">HTTP Method</th>
    <th class="special-bg">Description</th>
</thead>
<tr class="info-bg">
    <td class="centered" width="300px"><b>&nbsp;</b></td>
    <td><b>Retrieve</b> an existing <b>resource</b>.</td>
</tr>
<tr class="success-bg">
    <td class="centered" width="300px"><b>&nbsp;</b></td>
    <td><b>Create</b> a new <b>resource</b>.</td>
</tr>
<tr class="success-bg">
    <td class="centered" width="300px"><b>&nbsp;</b></td>
    <td><b>Update</b> an existing <b>resource</b>.</td>
</tr>
<tr class="caution-bg">
    <td class="centered" width="300px"><b>&nbsp;</b></td>
    <td><b>Partially update</b> an existing <b>resource</b>.</td>
</tr class="centered">
<tr class="danger-bg">
    <td class="centered" width="300px"><b>&nbsp;</b></td>
    <td><b>Delete</b> a <b>resource</b>.</td>
</tr>
<tbody>
</tbody>
</table>

[HTTP]: https://en.wikipedia.org/wiki/HTTP

---

# REST: <span class="gold">HTTP Status Codes</span>

It is important to check the [HTTP] <b>_________________________________</b> to
determine if the result of the <strong class="special">REST</strong> API was
successful:

<br>

<table class="bordered font-smaller">
<thead>
    <th class="special-bg">Code</th>
    <th class="special-bg">Meaning</th>
    <th class="special-bg">Description</th>
</thead>
<tbody>
<tr class="success-bg">
    <td class="centered" width="125px"><b>&nbsp;</b></td>
    <td>OK</td>
    <td>The requested action was <b>successful</b>.</td>
</tr>
<tr class="caution-bg">
    <td class="centered" width="125px"><b>&nbsp;</b></td>
    <td>Bad Request</td>
    <td>The request was <b>malformed</b>.</td>
</tr>
<tr class="caution-bg">
    <td class="centered" width="125px"><b>&nbsp;</b></td>
    <td>Not Found</td>
    <td>The requested resource was <b>not found</b>.</td>
</tr>
<tr class="caution-bg">
    <td class="centered" width="125px"><b>&nbsp;</b></td>
    <td>Method Not Allowed</td>
    <td>The requested method was <b>not supported</b>.</td>
</tr>
<tr class="danger-bg">
    <td class="centered" width="125px"><b>&nbsp;</b></td>
    <td>Internal Server Error</td>
    <td><b>Error</b> occurred when processing the request.</td>
</tr>
</tbody>
</table>

---

# REST: <span class="gold">Endpoints</span>

A <strong class="special">REST</strong> API describes [HTTP] methods and
<strong class="success"> _____________________________</strong>

(ie. <strong class="success">URL paths</strong>), along with any <strong
class="danger"> __________________________________</strong>.

<br>

<table class="bordered font-smaller">
<thead>
    <th class="special-bg">HTTP Method</th>
    <th class="special-bg">API Endpoint</th>
    <th class="special-bg">Description</th>
    <th class="special-bg">Query Data</th>
    <th class="special-bg">Form Data</th>
</thead>
<tbody>
<tr class="info-bg">
    <td class="centered"><b>GET</b></td>
    <td>/greeting</td>
    <td>Get greeting for <code>name</code></td>
    <td><code>name<code>: <code>str</code></td>
    <td></td>
</tr>
<tr class="success-bg">
    <td class="centered"><b>POST</b>/<b>PUT</b></td>
    <td>/greeting</td>
    <td>Set greeting to <code>greeting<code></td>
    <td></td>
    <td><code>greeting<code>: <code>str</code></td>
</tr>
</tbody>
</table>

---

# Vial: [hello_app.py]

> Implement [hello_app.py] using [Vial].

```bash
$ curl localhost:9999/greeting?name=Tin                         # Get greeting for Tin
Hello, Tin

$ curl --json '{"greeting": "Hola"}' localhost:9999/greeting    # Set greeting to Hola
{"greeting": "Hola", "default_name": "Unknown"}

$ curl localhost:9999/greeting?name=Huzz                        # Get greeting for Huzz
Hola, Huzz
```

[hello_app.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides27/hello_app.py
[Vial]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides27/vial.py
