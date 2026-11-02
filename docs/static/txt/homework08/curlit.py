#!/usr/bin/env python3

import hashlib
import json
import socket
import ssl
import sys

from dataclasses import dataclass
from typing import Optional
from urllib.parse import urlsplit

# Constants

CURLIT_DEFAULT_HEADERS = {'User-Agent': 'CurlIt/0.1'}
CURLIT_HTTP_VERSION    = 'HTTP/1.0'

# Classes

@dataclass
class HTTPConnection:
    host:       str
    port:       int
    use_ssl:    bool=False

    def __enter__(self):
        ''' Create socket connection to host and port.  Wrap socket if SSL is
        enabled.

        >>> with HTTPConnection('dredd.h4x0r.space', 80, False) as c: c.socket # doctest: +ELLIPSIS
        <socket.socket fd=...>

        >>> with HTTPConnection('dredd.h4x0r.space', 443, True) as c: c.socket # doctest: +ELLIPSIS
        <ssl.SSLSocket fd=...>
        '''
        # TODO
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        ''' Close socket. '''
        # TODO
        pass

@dataclass
class HTTPResponse:
    status:     str
    headers:    dict[str, str]
    text:       str

    def json(self) -> dict:
        ''' Return content as JSON.

        >>> get('https://useragent.in/api/me').json() # doctest: +ELLIPSIS
        {'ok': True, 'ua': ...}
        '''
        # TODO
        pass

    def content(self) -> bytes:
        ''' Return content as bytes.

        >>> get('http://weasel.h4x0r.space').content() # doctest: +ELLIPSIS
        b'<!DOCTYPE html>...'
        '''
        # TODO
        pass

    @property
    def status_code(self) -> int:
        ''' Return HTTP code from status

        >>> get('http://weasel.h4x0r.space').status_code
        200

        >>> get('http://pnutz.h4x0r.space').status_code
        301

        >>> get('http://weasel.h4x0r.space:9898/asdf').status_code
        404
        '''
        # TODO
        pass

# Functions

def usage(status: int=0) -> None:
    print('Usage: curlit [-v -H HEADER] URL', file=sys.stderr)
    sys.exit(status)

def get(url, headers: Optional[dict[str, str]]=None) -> HTTPResponse:
    ''' Perform HTTP GET on url

    >>> hashlib.sha1(get('http://weasel.h4x0r.space:9898/').content()).hexdigest()
    '781179f0e77978fabc99661fc159d22713d1419d'

    >>> hashlib.sha1(get('https://dredd.h4x0r.space').content()).hexdigest()
    'a6ef043f9397f574178164b9e93ebf54692e3e12'

    >>> get('https://ip.yld.me/User-Agent').text
    'CurlIt/0.1'

    >>> get('https://pnutz.h4x0r.space/courses/cse.20589.fa26/static/json/reading08.json').json()['q1']['type']
    'blank'
    '''
    # TODO: Parse URL, determine host, port, path, and scheme, update headers
    pass

    # TODO: Connect to remote server at parsed host and port
    pass

    # TODO: Send HTTP Request (Method, Headers, Sentinel)
    pass

    # TODO: Read HTTP Response (Status, Headers, Content)
    pass

    # TODO: Return HTTPResponse
    pass

def curlit(url: str, headers: Optional[dict[str, str]]=None, verbose: bool=False):
    ''' Perform HTTP GET on specified URL with given headers.  If verbose is
    enabled, then output status and headers before text.

    >>> curlit('http://weasel.h4x0r.space:9898/txt/hello.txt')
    hello, world!

    >>> curlit('https://ip.yld.me/Fake-Header', {'Fake-Header': 'Testing/1.2.3'})
    Testing/1.2.3

    >>> curlit('http://weasel.h4x0r.space:9898/txt/hello.txt', verbose=True) # doctest: +ELLIPSIS
    < HTTP/1.0 200 OK
    < Server: SimpleHTTP/0.6 Python/3.14.4
    < Date: ...
    < Content-type: text/plain
    < Content-Length: 14
    < Last-Modified: ...
    <
    hello, world!
    '''
    # TODO
    pass

# Main Execution

def main(arguments: list[str]=sys.argv[1:]) -> None:
    ''' Parse command line arguments and then performs HTTP GET on specified
    URL. '''
    # Parse command line arguments
    verbose = False
    headers = CURLIT_DEFAULT_HEADERS.copy()

    while arguments and arguments[0].startswith('-'):
        arguments.pop(0)
        # TODO
        pass

    if not arguments:
        usage(1)

    url = arguments[0]
    if '://' not in url:
        url = 'http://' + url

    # Perform HTTP Request
    try:
        # TODO
        pass
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
