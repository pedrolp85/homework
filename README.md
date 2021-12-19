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
git clone https://github.com/DenverCoder1/readme-typing-svg.git
cd readme-typing-svg
```

### Running the app locally

```bash
composer start
```

Open <http://localhost:8000/> and add parameters to run the project locally.

### Running the tests

Before you can run tests, PHPUnit must be installed. You can install it using Composer by running the following command.

```bash
composer install
```

Run the following command to run the PHPUnit test script which will verify that the tested functionality is still working.

```bash
composer test
```
### Clone the repository

```bash
git clone https://github.com/DenverCoder1/readme-typing-svg.git
cd readme-typing-svg
```

### Running the app locally

```bash
composer start
```

Open <http://localhost:8000/> and add parameters to run the project locally.

### Running the tests

Before you can run tests, PHPUnit must be installed. You can install it using Composer by running the following command.

```bash
composer install
```

Run the following command to run the PHPUnit test script which will verify that the tested functionality is still working.

```bash
composer test
```

