---
title: "Slides 27: REST, Vial"
description: "REST, Vial"
author: Peter Bui
keywords: lecture,sos,http,rest,vial
url: https://pnutz.h4x0r.space/courses/cse.20589.fa26/slides27.html
theme: domer-slides
---

<!-- _class: lead -->

# CSE 20589

## REST, Vial

---

# REST: <span class="gold">Overview</span>

<strong class="special">REST</strong> (<i><b>re</b>presentational **s**tate
**t**ransfer</i>) and is a <strong class="success">software architecture
style</strong> that defines a <strong class="strong">pattern</strong> for
<strong class="info">client</strong> and <strong class="danger">server</strong>
interactions.

<div class="columns">

<div class="font-smaller">

1. <strong class="success">Stateless</strong>: The <strong
   class="danger">server</strong> won't maintain any <strong
   class="warning">state</strong> between <strong
   class="caution">requests</strong> from the <strong
   class="info">client</strong>.

2. <strong class="info">Client</strong>-<strong class="danger">server</strong>:
   The <strong class="info">client</strong> and <strong
   class="danger">server</strong> must be <strong
   class="warning">decoupled</strong> from each other, allowing each to develop
   <strong class="success">independently</strong>.

3. <strong class="caution">Uniform interface</strong>: The <strong
   class="danger">server</strong> will provide a <strong
   class="caution">uniform interface</strong> for accessing <strong
   class="warning">resources</strong> without defining their representation.

</div>

<div class="centered">

<img src="static/img/software-systems.svg">

</div>

</div>

---

# REST: <span class="gold">HTTP Methods</span>

A <strong class="special">web application</strong> adheres to <strong
class="special">REST</strong> architecture constraints by exposing their data
(ie. <strong class="warning">resources</strong>) to the outside world through
an API accessible via public [HTTP] <strong class="success">URLs</strong>.

<table class="bordered font-smaller">
<thead>
    <th class="special-bg">HTTP Method</th>
    <th class="special-bg">Description</th>
</thead>
<tr class="info-bg">
    <td class="centered"><b>GET</b></td>
    <td>Retrieve an existing resource.</td>
</tr>
<tr class="success-bg">
    <td class="centered"><b>POST</b></td>
    <td>Create a new resource.</td>
</tr>
<tr class="success-bg">
    <td class="centered"><b>PUT</b></td>
    <td>Update an existing resource.</td>
</tr>
<tr class="caution-bg">
    <td class="centered"><b>PATCH</b></td>
    <td>Partially update an existing resource.</td>
</tr class="centered">
<tr class="danger-bg">
    <td class="centered"><b>DELETE</b></td>
    <td>Delete a resource.</td>
</tr>
<tbody>
</tbody>
</table>

[HTTP]: https://en.wikipedia.org/wiki/HTTP

---

# REST: <span class="gold">HTTP Status Codes</span>

When performing a [HTTP] operation, it is important to check the [HTTP]
**status code** to determine if the result of the <strong
class="special">REST</strong> API was successful:

<table class="bordered font-smaller">
<thead>
    <th class="special-bg">Code</th>
    <th class="special-bg">Meaning</th>
    <th class="special-bg">Description</th>
</thead>
<tbody>
<tr class="success-bg">
    <td class="centered"><b>200</b></td>
    <td>OK</td>
    <td>The requested action was successful.</td>
</tr>
<tr class="caution-bg">
    <td class="centered"><b>400</b></td>
    <td>Bad Request</td>
    <td>The request was malformed.</td>
</tr>
<tr class="caution-bg">
    <td class="centered"><b>404</b></td>
    <td>Not Found</td>
    <td>The requested resource was not found.</td>
</tr>
<tr class="caution-bg">
    <td class="centered"><b>405</b></td>
    <td>Method Not Allowed</td>
    <td>The requested method was not supported.</td>
</tr>
<tr class="danger-bg">
    <td class="centered"><b>500</b></td>
    <td>Internal Server Error</td>
    <td>Error occurred when processing the request.</td>
</tr>
</tbody>
</table>

---

# REST: <span class="gold">Endpoints</span>

To define a <strong class="special">REST</strong> API, it is necessary to
describe the [HTTP] methods and <strong class="success">endpoints</strong> (ie.
<strong class="success">URL paths</strong>), along with any <strong
class="danger">parameters</strong> they may take.

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

# Vial: <span class="gold">Overview</span>

[Vial] is **micro-framework** based on <strong
class="success">Python</strong>'s built-in [HTTPserver] and is similar in
design to [flask] and [bottle].

<div class="columns">

<div>

```python
# Hello, World in Vial
from vial import Vial

App = Vial()

@App.route('/')
def hello(request):
    return 'Hello, world!'

App.run()
```

</div>

<div class="middled font-smaller">

- [Vial] wraps the [HTTPServer] class with a custom `VialHTTPRequestHandler`
  that provides utility methods for reading <strong
  class="caution">request</strong> data and writing <strong
  class="warning">responses</strong>.

- User declares a <strong class="danger">global</strong> `App` instance of [Vial].

- User maps <strong class="success">functions</strong> to specific <strong
  class="special">routes</strong> using a [decorator].

</div>

</div>

[flask]: https://flask.palletsprojects.com/en/stable/
[bottle]: https://bottlepy.org/docs/dev/
[Vial]: https://github.com/nd-cse-20589-fa26/examples/blob/master/slides27/vial.py
[decorator]: https://docs.python.org/3/glossary.html#term-decorator
[HTTPServer]: https://docs.python.org/3/library/http.server.html#http.server.HTTPServer

---

# Vial: <span class="gold">Super()</span>

The `Vial` <strong class="caution">class</strong> inherits from [HTTPServer].
Therefore, it uses [super] during construction to call the `__init__` of its
<strong class="warning">parent</strong>.

```python
# Vial Application Class
class Vial(HTTPServer):
    def __init__(self, host: str='127.0.0.1', port: int=8080, attributes=None):
        # Call __init__ of HTTPServer
        super().__init__((host, port), VialRequestHandler)
        ...
```

<div class="font-smaller">

[super] uses the [Method Resolution Order] to determine which
<strong class="caution">class</strong> to call next:

1. <strong class="caution">Subclasses</strong> always come before their <strong
   class="warning">parents</strong>.

2. The order of <strong class="warning">parents</strong> specified in the
   <strong class="caution">class</strong> definition is preserved (<b><i
   class="muted">left-to-right</i></b>).

</div>

[super]: https://docs.python.org/3/builtins/functions.html#super
[Method Resolution Order]: https://docs.python.org/3/howto/mro.html

---

# Vial: <span class="gold">setattr</span>

The `Vial` <strong class="caution">class</strong> allows the user to specify
custom <strong class="info">attributes</strong> which can be used in lieu of
<strong class="danger">global</strong> variables:

```python
# Vial Application Class
class Vial(HTTPServer):
    def __init__(self, host: str='127.0.0.1', port: int=8080, attributes=None):
        ...
        if attributes:  # Add attributes to object instance at run-time
            for key, value in attributes.items():
                setattr(self, key, value)
```

<div class="font-smaller">

The [setattr] function adds (or updates) an <strong class="info">attribute</strong> to the given
<strong class="primary">object</strong> instance with the given `value`.  Similarly,
[getattr] can be used to read the value of a given <strong class="info">attribute</strong>.

</div>

[setattr]: https://docs.python.org/3/builtins/functions.html#setattr
[getattr]: https://docs.python.org/3/builtins/functions.html#getattr

---

# Vial: <span class="gold">Cached Properties</span>

The `Vial` <strong class="caution">class</strong> uses a custom
`VialRequestHandler` to process <strong class="info">client</strong> connections.

<table class="bordered font-smaller">
<thead>
    <th class="special-bg">Cached Property</th>
    <th class="special-bg">Description</th>
</thead>
<tbody>
<tr class="success-bg">
    <td class="centered"><b>url</b></td>
    <td>Returns parsed <code>URL</code> structure from request path.</td>
</tr>
<tr class="danger-bg">
    <td class="centered"><b>query_data</b></td>
    <td>Returns <code>dict</code> of parsed query string from <code>URL</code>.</td>
</tr>
<tr class="caution-bg">
    <td class="centered"><b>post_data</b></td>
    <td>Returns read <code>POST</code> data payload.</td>
</tr>
<tr class="warning-bg">
    <td class="centered"><b>form_data</b></td>
    <td>Returns <code>dict</code> of parsed <code>POST</code> data payload (<i class="muted">possibly JSON</i>).</td>
</tr>
</tbody>
</table>

<br>

<div class="alert info-bg">

These **cached properties** come from [RealPython].

</div>

[RealPython]: https://realpython.com/python-http-server/#serve-static-and-dynamic-content-programmatically

---

# Vial: <span class="gold">Writing Text</span>

As discussed in lecture, most [HTTP] <strong class="warning">responses</strong>
have the same structure: 1. [HTTP] **status_code**, 2. [HTTP] **headers**, 3.
[HTTP] body.

```python
def write_text(self, text: str, status_code: int=200, mimetype: str='text/plain'):
    self.send_response(status_code)             # HTTP Status Code
    self.send_header('Content-Type', mimetype)  # HTTP Headers
    self.end_headers()
    self.wfile.write(text.encode())             # HTTP Body

def write_error(self, status_code: int):        # Lookup HTTP error status string
    self.write_text(responses[status_code], status_code=status_code)
```

<br>

<div class="alert danger-bg font-smaller">

[http.client.responses] is a **dictionary** that maps [HTTP] **status codes**
to their corresponding **strings**.

</div>

[http.client.responses]: https://docs.python.org/3/library/http.client.html#http.client.responses

---

# Vial: <span class="gold">Routes</span> (<i class="muted">Implementation</i>)

To allow different **functions** to handle separate <strong
class="success">endpoints</strong>, the `Vial` <strong
class="caution">class</strong> provides a `route` [decorator]:

```python
class VialRequestHandler(BaseHTTPRequestHandler):
    # Routes dict {method: {pattern: callback}}
    Routes: dict[str, dict[str, Callable]] = {}

class Vial(HTTPServer):
    def route(self, pattern: str, methods: list[str]=['GET']):  # Route Decorator factory
        def decorator(callback):                                # Route Decorator function
            for method in methods:                              # Add pattern/callback to Routes dict
                try:              VialRequestHandler.Routes[method].update({pattern: callback})
                except KeyError:  VialRequestHandler.Routes[method] = {pattern: callback}
            return callback
        return decorator
```

---

# Vial: <span class="gold">Routes</span> (<i class="muted">Usage</i>)

<div class="columns">

<div>

To map a `route`, we use the [decorator] to <strong
class="comment">annotate</strong> a **function**:

```python
App = Vial()            # Create instance of Vial

@App.route('/')
def hello(request):     # Route / to hello function
    return 'Hello, World'

@App.route('/upload', methods=['PUT'])
def upload(request):    # Route /upload to upload function
    return {'body': request.post_data}
```

</div>

<div>

Unwrapping the `route` [decorator] would be equivalent to:

```python
def hello(request):
    return 'Hello, World'

def upload(request):
    return {'body': request.post_data}

# App.route('/') -> returns decorator
# decorator(hello) -> registers routers and returns hello
hello = App.route('/')(hello)

# App.route('/upload', methods=['PUT']) -> returns decorator
# decorator(hello) -> registers routers and returns hello
upload = App.route('/upload', methods=['PUT'])(upload)
```

</div>
</div>

---

# Vial: <span class="gold">Method Dispatch</span>

To dispatch the `route` <strong class="success">callbacks</strong>, we use a
generalized `do_METHOD`:

```python
def do_METHOD(self, method: str):
    if not method in VialRequestHandler.Routes: return self.write_error(405)    # Check if method is in Routes

    for pattern, callback in VialRequestHandler.Routes[method].items():         # Loop through all callbacks for method
        if matched := re.fullmatch(pattern, self.url.path):                     # Check if pattern matches full URL path
            result = callback(self, *matched.groups())                          # Execute callback and collect results
            match result:                                                       # Process result based on type
                case int():  return self.write_error(result)
                case str():  response, *args = result, 200, 'text/plain'
                case dict(): response, *args = json.dumps(result), 200, 'application/json'
                case None:   response, *args = '', 200, 'text/plain'
                case _:      response, *args = result
            return self.write_text(response, *args) # type: ignore[arg-type]
    return self.write_error(405)
```

<br>

<div class="alert success-bg font-smaller">

The `do_METHOD` checks the `result` of the <strong class="success">callback</strong> and will
call `write_text` with the appropriate `text`, `status_code`, and `mimetype`.

</div>

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
