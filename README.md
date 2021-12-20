# RHEL homework

This Repository contains a Python app that satisfies the following requirements:

Interview app - log parsing utility v1.02:
-----------------------------------------------------------------------------------
Create a Python CLI application that will help you parse logs of various
kinds. The code should be easy to deploy and run and must be hosted in
a publicly available git repository. A test suite must be included as well.
Your solution can be as robust or as minimal as you want but please keep in
mind that this is your opportunity to show us what you can do. :)

You may leverage any open source Python library.
You may not leverage the 'head', 'tail' or 'grep' utilities.

Usage: ./util.py [OPTION]... [FILE]

Supported options:

```bash
  -h, --help         Print help
  -f, --first NUM    Print first NUM lines
  -l, --last NUM     Print last NUM lines
  -t, --timestamps   Print lines that contain a timestamp in HH:MM:SS format
  -i, --ipv4         Print lines that contain an IPv4 address, matching IPs
                     are highlighted
  -I, --ipv6         Print lines that contain an IPv6 address (standard
                     notation), matching IPs are highlighted

If FILE is omitted, standard input is used instead.
If multiple options are used at once, the result is the intersection of their
results.

The result (matching lines) is printed to standard output.
```

### Clone the repository

```bash
$ git clone https://github.com/pedrolp85/homework.git
$ cd homework
```


### Running the app inside a container

A docker-compose file is provided which buids 2 services, one for the prod app (util), an another one that runs Pytest inside the container (tests)
Before you can run it, docker engine and docker-compose must be installed.


```bash
$ docker-compose build util
$ ./util.sh [OPTION]... [FILE]
```
Please Notice that if you provide a [FILE] argument in an absolute or relative path, the App will look into the container filesystem
if you want to test the app with a file on the host, provide the input with stdin
Test files are provided in the path tests/test_files, you can leave there your own test files and rebuild the image so the new files
will be con the container too

Examples:

Input file in container FileSystem:

```bash
$ ./util.sh --first 10 tests/test_files/intersection.log
```

Input file in your host or virtual Machine:

```bash
$ cat /etc/shadow | ./util.sh
```

Adding new files to the container

```bash
$ cp some_file.log app/tests/test_files/
$ docker-compose build util
$ ./util.sh --first 10 tests/test_files/some_file.log
```

### Running the tests inside the container

Pytest is included in the package section of the Pipfile (instead of package-dev section as usual) just in case you want to run the test
suite inside the container
Another image is buid with another entrypoint that runs pytest and exits the container

```bash
docker-compose build tests
./test.sh
```


### Running the app locally on your host or virtual machine

As executed in a host or virtual machine, the app will use a virtual env instead of using system Python.
Python 3.7 and pipenv are required in your system

```bash
$ https://github.com/pedrolp85/homework.git
$ cd homework
$ pipenv lock
$ pipenv install
$ pipenv shell
$ cd app
$ python util.py --ipv4 192.168.1.1 --ipv6 2001:db8:0:0:0::1 tests/test_files/intersection.log
```

### Running the tests locally on your host or virtual machine

```bash
$ https://github.com/pedrolp85/homework.git
$ cd homework
$ pipenv lock
$ pipenv install
$ pipenv shell
$ cd app
$ pytest
```



## Some Cool Features
==============================================================================

Let's see some examples of what our app can do


## --first *value* (-f *value*)

Supports integer input to show the first *value* lines of the file or stdin

* If int = 0, no output will be shown
* if int < 0 , the output will be the same as --last abs(int)
* Any input that is not an integer, will rise a **Value Error**

## --last *value* (-l *value*)

Supports integer input to show the last *value* lines of the file or stdin

* If int = 0, no output will be shown
* if int < 0 , the output will be the same as --first abs(int)
* Any input that is not an integer, will rise a **Value Error**

## --ipv4 *IPv4Adress* (-i *IPv4Adress*)

Supports ipv4 address input to show the lines that contain that IP address ( matching IP addresses will be highlighted)

* Support integer and dot-decimal IPv4 representation even if the text has different representation (does not act as a regex finder)
* Any input that is not a valid ipv4 address, will rise a **Value Error**

Example:

```bash
$ cat tests/test_files/intersection.log
L1 172.16.0.1 
L2 192.168.1.255 172.16.0.10 2001:db8:0::1

$ ./util.sh --ipv4 3232236031 tests/test_files/intersection.log
L2 *192.168.1.255* 172.16.0.10 2001:db8:0::1

```

## --ipv6 *IPv6Adress* (-I *IPv6Adress*)

Supports ipv6 address input to show the lines that contain that IP address ( matching IP addresses will be highlighted)

* Supports several IPv6 representations, and finds the IPv6 address even if the file has a differente representation
* Any input that is not a valid ipv6 address, will rise a **Value Error**

```bash
$ cat tests/test_files/ipv6.log
2001:db8:0:0:0::1
2001:db8:0:0::1
2001:db8:0::1
2001:db8::1
2001:db8:0:0:0::1 2001:db8:0:0::1 2001:db8:0::1 2001:db8::1

$ ./util.sh --ipv6 2001:db8:0:0:0::1 tests/test_files/ipv6.log
2001:db8:0:0:0::1
2001:db8:0:0::1
2001:db8:0::1
2001:db8::1
2001:db8:0:0:0::1 2001:db8:0:0::1 2001:db8:0::1 2001:db8::1

```

## --timestamps *HH:MM:SS* (-t *HH:MM:SS*)

Supports a timedate input to search in log files

* The input must be zero padded to fill the format, any other input will rise **Value Error**

## no options

The app will return the full file or stdin input

## [FILE]

Supports both relative and absolute paths
Relative paths will start in homework/app/

* Non-Existing files will rise a message (The File provided does not exist) and the app will exit with code 2 
* Permission error will rise a message (Permission denied to operate the file) and the app will exit with code 2