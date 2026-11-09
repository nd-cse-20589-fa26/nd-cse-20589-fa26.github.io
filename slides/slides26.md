---
title: "Slides 26: Web Applications"
description: "Web Applications"
author: Peter Bui
keywords: lecture,sos,http,web applications
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides26.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## Web Applications

---

# Web Applications: <span class="gold">Overview</span>

A <strong class="special">web application</strong> is a <strong
class="success">software system</strong> that uses the <strong
class="info">client</strong> / <strong class="danger">server</strong> model to
provide dynamic and interactive services.

<div class="columns">

<div class="font-smaller">

1. <strong class="info">Client-side (*Front-end*)</strong>: This is what you see
   and interact with (typically inside your **web browser**) and is built with
   [HTML], [CSS], and [JavaScript].

2. <strong class="danger">Server-side (*Back-end*)</strong>: This is what handles
   the data storage and processing user requests via [HTTP] and is built with
   languages like [Python], [PHP], or [Node.js].

</div>

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

To implement the [HTTP] <strong class="danger">back-end</strong> of a <strong
class="special">web application</strong> in [Python], we can use the builtin
[HTTPServer].

```python
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Create a HTTP server that listens on port 9999 of every IP address
server = HTTPServer(('0.0.0.0', 9999), SimpleHTTPRequestHandler)
server.serve_forever()
```

Every time a [HTTP] <strong class="info">client</strong> is `accepted` by the
<strong class="danger">server</strong>, a [SimpleHTTPRequestHandler] object is
created to process that connection.

[HTTPServer]: https://docs.python.org/3/library/http.server.html#http.server.HTTPServer
[SimpleHTTPRequestHandler]: https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler

---

# Web Applications: <span class="gold">Concurrency</span>

[HTTPServer] handles one [HTTP] connection at a time.  To add <strong
class="success">concurrency</strong> we can either use [ThreadingHTTPServer] in
place of [HTTPServer] or create our own `ForkingHTTPServer` by using <strong
class="special">multiple inheritance</strong>.

```python
from socketserver import ForkingMixIn

# Create custom Forking HTTPServer by inheriting ForkingMixIn
class ForkingHTTPServer(ForkingMixIn, HTTPServer):
    ''' Multi-process HTTP server that forks a new process per request. '''
    max_children = 8    # Limit the number of concurrent processes

# Create a Forking HTTP server that listens on port 9999 of every IP address
server = ForkingHTTPServer(('0.0.0.0', 9999), SimpleHTTPRequestHandler)
server.serve_forever()
```

[ThreadingHTTPServer]: https://docs.python.org/3/library/http.server.html#http.server.ThreadingHTTPServer

---

# Web Applications: <span class="gold">Custom Handlers</span>

The provided [SimpleHTTPRequestHandler] serves files from the current
directory.  If we wish to create our own <strong
class="special">handler</strong>, then we need to <strong
class="caution">subclass</strong> [BaseHTTPRequestHandler]:

```python
class HelloRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):                                   # Implement HTTP Method
        self.send_response(200)                         # Send HTTP Status
        self.send_header('Content-Type', 'text/plain')  # Send HTTP Headers
        self.end_headers()
        self.wfile.write(f'Hello, World'.encode())      # Send HTTP Response
```

<div class="font-smaller">

This `HelloRequestHandler` will be used to create a <strong
class="special">handler</strong> object for every incoming connection.  If the
requested [HTTP] method is a `GET` then the `do_GET` method of this <strong
class="special">handler</strong> object will be called.

</div>

[BaseHTTPRequestHandler]: https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler

---

# Web Applications: <span class="gold">Query Data</span>

As discussed previously, a [HTTP] request may have a <strong
class="danger">query string</strong> which contains **key/value** pairs.  To
access this data, we can use the following utility methods from [RealPython]:

```python
class HelloRequestHandler(BaseHTTPRequestHandler):
    @cached_property
    def url(self):          return urlparse(self.path)              # Parse path into URL structure

    @cached_property
    def query_data(self):   return dict(parse_qsl(self.url.query))  # Parse URL query into dictionary

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        name = self.query_data.get('name', 'Unknown')               # Lookup name in query dictionary
        self.wfile.write(f'Hello, {name}!'.encode())
```

[RealPython]: https://realpython.com/python-http-server/#serve-static-and-dynamic-content-programmatically

---

# Web Applications: <span class="gold">Form Data</span>

For a [HTTP] `POST` request, the user may upload a data **payload**.  To access
this data, we can use the following utility methods from [RealPython]:

```python
class HelloRequestHandler(BaseHTTPRequestHandler):
    default_name: str='Unknown'                                     # Class attribute

    @cached_property                                                # Read Post data payload
    def post_data(self): return self.rfile.read(int(self.headers.get('Content-Length', 0)))

    @cached_property                                                # Parse Post data payload
    def form_data(self): return dict(parse_qsl(self.post_data.decode('utf-8')))

    def do_POST(self):                                              # Lookup name in Post form data
        HelloRequestHandler.default_name = self.form_data.get('name')
        self.send_response(200); self.send_header('Content-Type', 'text/plain'); self.end_headers()
        self.wfile.write(f'Default name is {HelloRequestHandler.default_name}'.encode())
```

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
