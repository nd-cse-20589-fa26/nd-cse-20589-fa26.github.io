#!/usr/bin/env python3

import html
import os
import re
import requests
import sys

from typing import Optional

# Constants

DEFAULT_ZIPCODE = 46556
WEATHER_URL     = 'https://forecast.weather.gov/zipcity.php'

# Functions

def usage(status: int=0):
    print(f'''Usage: weather [-c] ZIPCODE
    -c    Use Celsius degrees instead of Fahrenheit for temperature

If zipcode is not provided, then it defaults to {DEFAULT_ZIPCODE}.''', file=sys.stderr)
    sys.exit(status)

def weather(zipcode: int, url: str=WEATHER_URL, celsius: bool=False) -> tuple[Optional[str], Optional[str]]:
    ''' Return the temperature and forecast for the given zipcode using
    information at the specified url.

    If celsius is True, then return temperature in Celsius rather than
    Fahrenheit.

    >>> weather(46556, url='https://yld.me/raw/itJg')
    ('76°F', 'Overcast')

    >>> weather(46556, url='https://yld.me/raw/itJg', celsius=True)
    ('24°C', 'Overcast')
    '''
    # Fetch weather information
    pass

    # Extract temperature and forecast information
    pass

# Main Execution

def main(arguments: list[str]=sys.argv[1:]) -> None:
    ''' Print temperature and forecast for given zipcode.

    This function will parse the command line arguments to determine whether or
    not the temperature should be in Fahrenheit or Celsius.

    >>> main(['46556'])         # doctest: +ELLIPSIS
    Temperature: ...F
    Forecast:    ...

    >>> main(['-c', '46556'])   # doctest: +ELLIPSIS
    Temperature: ...C
    Forecast:    ...
    '''
    # Parse command line arguments
    pass

    # Get weather information and print it out
    pass

if __name__ == '__main__':
    main()
