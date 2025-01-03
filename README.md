# quick-conn-test

Quick Connection Tester

Used for quickly testing out host/port pairs. Note this has very limited error trapping and may not handle unusual edge cases well (or perhaps not at all).

## Prerequisites

Requires Python 3.x (preferably 3.6+) and uses the following (entirely standard) libraries:
* sys
* socket
* argparse

## How to Use

```
./quick-conn-test.py --help
usage: quick-conn-test.py [-h] -a HOST -p PORT [-t TIMEOUT]

optional arguments:
  -h, --help            show this help message and exit
  -a HOST, --host HOST  Host or IP address to test
  -p PORT, --port PORT  Port number to test
  -t TIMEOUT, --timeout TIMEOUT
                        Set timeout in seconds
```

Timeout values are approximate. A default value of 30 seconds is present in the event a timeout value is not specified by the user.
Examples:

```
./quick-conn-test.py --host localhost --port 22
Connection successful
```

```
./quick-conn-test.py --host localhost --port 21 --timeout 10
[Errno 111] Connection refused
```

```
./quick-conn-test.py --host www.google.com --port 21 --timeout 10
timed out
```

# Signaling

Standard *Nix-style messaging and exit codes apply:
* Successful output will be written to 'stdout' and exit code '0' will be issued for successful connections.
* Error messages will be written to 'stderr' and exit code '1' will be issued for connection errors/failures.

Efforts have been made to try to make this utility 'script-friendly' and generally easy to include into automation and scripted workflows.

## Built With

* [Python](https://www.python.org/) Designed by Guido van Rossum.

## Author

**Rick Pelletier** - [Gannett Co., Inc. (USA Today Network)](https://www.usatoday.com/)

