#!/usr/bin/env python3

from dataclasses import dataclass
from typing      import Iterable, Optional

import itertools
import os
import signal
import sys
import time

# Classes

@dataclass
class Timer:

    command:    list[str]
    timeout:    int = 1
    timedelta:  float = 0.1

    spinner:    Iterable[str] = itertools.cycle(r'/-\|')
    elapsed:    float = 0.0
    pid:        Optional[int] = None
    status:     Optional[int] = None

    # Context Manager

    def __enter__(self):
        ''' Fork child process.

        - Child: execute command and exit if unsuccessful.
        - Parent: register signal handlers and set alarm with timeout.

        Return current instance.

        >>> t = Timer(['true']).__enter__()
        >>> time.sleep(0.1)
        >>> all([t.pid is not None and t.pid > 0,
        ...      signal.getsignal(signal.SIGALRM) == t.handle_sigalrm,
        ...      signal.getsignal(signal.SIGCHLD) == t.handle_sigchld,
        ...      signal.alarm(0) > 0,
        ...      t.status is not None or os.wait() == (t.pid, 0)])
        True
        '''
        pass # TODO

    def __exit__(self, exc_type, exc_val, exc_tb):
        ''' Cancel alarm and wait for child.

        >>> t = Timer(['true']).__enter__()
        >>> time.sleep(0.1) and t.__exit__(None, None, None)
        >>> all([t.pid is not None and t.pid > 0, t.status is not None])
        True
        '''
        pass # TODO
    
    # Signal Handlers

    def handle_sigalrm(self, signum, frame):
        ''' Handle SIGALRM by sending process SIGTERM and then SIGKILL.

        >>> with Timer(['sleep', '5']) as t: time.sleep(t.timeout)
        >>> all([t.pid is not None and t.pid > 0, t.status == signal.SIGTERM])
        True
        '''
        try:
            pass # TODO
        except ProcessLookupError:
            pass

    def handle_sigchld(self, signum, frame):
        ''' Handle SIGCHLD by waiting for process if not waited yet.

        >>> with Timer(['sleep', '5']) as t: time.sleep(t.timeout)
        >>> all([t.pid is not None and t.pid > 0, t.status == signal.SIGTERM])
        True
        '''
        try:
            pass # TODO
        except ChildProcessError:
            pass

    # Iterator

    def __iter__(self):
        ''' Return current instance.

        >>> t = Timer(['true'])
        >>> iter(t) == t
        True
        '''
        pass # TODO

    def __next__(self):
        ''' Return elapsed time or stop iteration.

        - Check status to determine whether or not to end iteration.
        - Sleep timedelta and then increment elapsed by time delta.
        - Return elapsed time if timeout has not ben reached.

        >>> [f'{elapsed:0.1f}' for elapsed in Timer(['sleep', '2'])]
        ['0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0']
        '''
        # TODO
        raise StopIteration

    # Property

    @property
    def state(self):
        ''' Return status string

        - If process is still running, then return next spinner string.
        - Otherwise, process is terminate, so return 'Success', 'Failure',
          'Terminated', 'Killed' based on exit status.

        >>> all([Timer(['true']).state == '/',
        ...      Timer(['true'], status=0).state == 'Success',
        ...      Timer(['true'], status=256).state == 'Failure',
        ...      Timer(['true'], status=signal.SIGTERM).state == 'Terminated',
        ...      Timer(['true'], status=signal.SIGKILL).state == 'Killed'])
        True
        '''
        pass # TODO

    @property
    def returncode(self):
        ''' Return exit status if process exited, otherwise terminate signal.

        >>> all([Timer(['true'], status=0).returncode == 0,
        ...      Timer(['true'], status=256).returncode == 1,
        ...      Timer(['true'], status=signal.SIGTERM).returncode == signal.SIGTERM,
        ...      Timer(['true'], status=signal.SIGKILL).returncode == signal.SIGKILL])
        True
        '''
        pass # TODO

# Functions

def usage(status: int=0) -> None:
    print('''Usage: timeit.py [-d TIMEDELTA -t TIMEOUT] COMMAND...

    -d  TIMEDELTA   Amount of time to sleep between iterations (default: 0.1 s)
    -t  TIMEOUT     Amount of time to wait before killing process (default: 1 s)
''', file=sys.stderr)
    sys.exit(status)

# Main Execution

def main(arguments: list[str]=sys.argv[1:]) -> None:
    ''' Executes given command for specified timeout and shows status every
    timedelta. '''
    # Parse command line options
    timedelta = 0.1
    timeout   = 1
    command   = None

    pass # TODO

    # Execute command using timer, display elapsed time, exit with returncode
    pass # TODO

if __name__ == '__main__':
    main()
