#!/usr/bin/env python3

import fnmatch
import os
import sys

from abc import ABC, abstractmethod
from dataclasses import dataclass
from itertools import chain
from pathlib import Path

# Classes

class UnknownFilter(Exception):
    pass

class BaseFilter(ABC):
    ''' Filter Interface'''
    @abstractmethod
    def check(self, path: Path) -> bool:
        pass

class FileFilter(BaseFilter):
    ''' Filter: -type f '''
    def check(self, path: Path) -> bool:
        ''' Return true if path is a file (and not a symlink).

        >>> FileFilter().check(Path('/bin/find'))
        True
        '''
        # TODO
        return False

class DirectoryFilter(BaseFilter):
    ''' Filter: -type d '''
    def check(self, path: Path) -> bool:
        ''' Return true if path is a directory (and not a symlink).

        >>> DirectoryFilter().check(Path('/bin/find'))
        False
        '''
        # TODO
        return False

@dataclass
class NameFilter(BaseFilter):
    ''' Filter: -name PATTERN '''

    pattern: str

    def check(self, path: Path) -> bool:
        ''' Return true if name of file matches shell pattern

        >>> NameFilter('*nd').check(Path('/bin/find'))
        True
        '''
        # TODO
        return False

class EmptyFilter(BaseFilter):
    ''' Filter: -empty '''
    def check(self, path: Path) -> bool:
        ''' Return true if path is empty (must be file or directory, not symlink).

        >>> EmptyFilter().check(Path('/bin/find'))
        False
        '''
        # TODO
        return False

class ReadableFilter(BaseFilter):
    ''' Filter: -readable '''
    def check(self, path: Path) -> bool:
        ''' Return true if path is readable.

        >>> ReadableFilter().check(Path('/bin/find'))
        True
        '''
        # TODO
        return False

class WritableFilter(BaseFilter):
    ''' Filter: -writable '''
    def check(self, path: Path) -> bool:
        ''' Return true if path is writable.

        >>> WritableFilter().check(Path('/bin/find'))
        False
        '''
        # TODO
        return False

class ExecutableFilter(BaseFilter):
    ''' Filter: -executable '''
    def check(self, path: Path) -> bool:
        ''' Return true if path is executable.

        >>> ExecutableFilter().check(Path('/bin/find'))
        True
        '''
        # TODO
        return False

class FilterFactory:
    @classmethod
    def get_filter(cls, arguments: list[str]) -> BaseFilter:
        ''' Returns concrete Filter class based on arguments

        >>> FilterFactory.get_filter('-type f'.split()) # doctest: +ELLIPSIS
        <findit.FileFilter object at 0x...>

        >>> FilterFactory.get_filter('-type d'.split()) # doctest: +ELLIPSIS
        <findit.DirectoryFilter object at 0x...>

        >>> FilterFactory.get_filter('-name *.conf'.split()) # doctest: +ELLIPSIS
        NameFilter(pattern='*.conf')

        >>> FilterFactory.get_filter('-empty'.split()) # doctest: +ELLIPSIS
        <findit.EmptyFilter object at 0x...>

        >>> FilterFactory.get_filter('-readable'.split()) # doctest: +ELLIPSIS
        <findit.ReadableFilter object at 0x...>

        >>> FilterFactory.get_filter('-writable'.split()) # doctest: +ELLIPSIS
        <findit.WritableFilter object at 0x...>

        >>> FilterFactory.get_filter('-executable'.split())  # doctest: +ELLIPSIS
        <findit.ExecutableFilter object at 0x...>
        '''
        # TODO
        raise UnknownFilter

# Functions

def usage(status: int=0):
    ''' Print usage message and exit with status. '''
    print(f'''Usage: findit ROOT [FILTERS]

Filters:
    -type [f|d]     File is of type f for regular file or d for directory
    -name PATTERN   Name of file matches shell pattern
    -empty          File or directory is empty
    -readable       File is readable by user
    -writable       File is writable by user
    -executable     File is executable or directory is searchable by user
''', file=sys.stderr)
    sys.exit(status)

def walk(root: Path, filters: list[BaseFilter]) -> None:
    ''' Print root if it passes all filters and then recursively walk root and
    print any entries that pass all filters. '''
    # TODO
    pass

def main(arguments: list[str]=sys.argv[1:]):
    ''' Parse command line arguments to get root and filters, and then walk
    root using specified filters. '''
    # TODO: Parse root command line argument
    pass

    # TODO: Parse filters command line arguments
    pass

    # TODO: Walk root with filters
    pass

# Main Execution

if __name__ == '__main__':
    main()
