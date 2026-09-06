#!/usr/bin/env python3

import html
import os
import re
import requests
import sys
import textwrap

# Constants

PLACEMARKS_URL = 'https://map.nd.edu/placemarks.json'
INDENT         = ' '*6

# Functions

def usage(status: int=0):
    print(f'''Usage: campus [-n LIMIT -t TAGS] NAME
    -n LIMIT    Only display up to LIMIT results
    -t TAGS     Search for specified TAGS

You may either search by NAME or by TAGS, but not both at the same time.
''', file=sys.stderr)
    sys.exit(status)

def clean_description(html: str) -> str:
    ''' Clean description by removing images, links, replacing newlines with a
    space, removing tags, and then stripping the final result.

    >>> clean_description('<img src=...><p>Go Irish</p><a href=...>Link</a>')
    'Go Irish'
    '''
    pass

def campus(query: str, tags: list[str], limit: int=5) -> None:
    ''' Search campus placemarks based on query or tags and display up to limit
    results.  For tags, results should match all tags.

    >>> campus('cushing', [])
       1. Cushing Hall of Engineering (125) [building,core]
    <BLANKLINE>
          Opened in 1933, the exterior is embellished with the names of
          history's great scientists and engineers, as well as traditional
          engineering tools. The lobby includes intricate mosaics and a
          ceiling decorated with botanical and geometric forms.
    '''
    pass

# Main Execution

def main(arguments: list[str]=sys.argv[1:]) -> None:
    ''' Searches campus placemarks based on name or tags and displays to a
    certain limit of results.

    >>> main(['-n', '1', 'fitz'])
       1. Fitzpatrick Hall of Engineering (126) [green,building,core]
    <BLANKLINE>
          Opened in 1979, it is the primary location for engineering
          teaching, research and computing.  The roof of Fitzpatrick Hall
          is home to a  and monitoring system.  The panels lie flat and
          are attached directly to the surface of the roof, and are
          connected directly to the University's power grid, helping meet
          Fitzpatrick's electricity demand.
    '''
    # Parse command line arguments
    pass

    # Search campus based on query or tags
    pass

if __name__ == '__main__':
    main()
