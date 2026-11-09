---
title: "Notebook 26: Web Applications"
description: "Web Applications"
author: Peter Bui
keywords: notebook,sos,http,web applications
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/notebook26.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Web Applications

---

# Web Applications: <span class="gold">Overview</span>

A <strong class="special">web application</strong> is a <strong
class="success">software system</strong> that uses <strong>__________________</strong>.

<br>

<div class="centered">

<img src="static/img/software-systems.svg">

</div>

</div>

[HTML]: https://en.wikipedia.org/wiki/HTML
[CSS]: https://en.wikipedia.org/wiki/CSS
[JavaScript]: https://en.wikipedia.org/wiki/JavaScript
[HTTP]: https://en.wikipedia.org/wiki/HTTP
[Python]: https://python.org
[PHP]: https://www.php.net/
[Node.js]: https://nodejs.org/en

---

# Web Applications: <span class="gold">HTTP Server</span>

<div class="slide-centered">

<img src="static/img/slides25-http-server-blank.svg">

</div>

---

# Web Applications: [hello_app.py]

> Write a simple **Hello, World** <strong class="special">web
> application</strong> that says hello to the user and let's the user specify
> the default name if none is specified.

```bash
$ ./hello_app.py localhost 9999             # Start Hello Web Application

$ curl localhost:9999/?name=Domer           # Get greeting
Hello, Domer

$ curl -d 'name=Irish' localhost:9999/      # Set default name
Default name is Irish
```

[hello_app.py]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides26/hello_app.py
