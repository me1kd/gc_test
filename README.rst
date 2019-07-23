=======
gc_test
=======


This is a command-line programm that aims to resolve the supermarket checkout problem describe in coding challenge.


Description
===========

Usage
-----

Prerequisites
^^^^^^^^^^^^^
1. Python >= 3.4
2. sqlite3

Installation
^^^^^^^^^^^^
1. cd into the root directory
2. execute command: **python setup.py install**

Run program
^^^^^^^^^^^
usage: gccalc [-h] [--version] [-v] [-vv] STRING

A total price calculator

positional arguments:
  STRING               String formed by SKU chars

optional arguments:
  -h, --help             show this help message and exit
  --version              show program's version number and exit
  -v, --verbose          set loglevel to INFO
  -vv, --very-verbose    set loglevel to DEBUG

Example
^^^^^^^
| >gccalc ABCDE453
| The product ABCDE453 total price is 115.0
| The skus ['3', 'E', '4', '5'] are not in system and not counted in.

Test
^^^^
Test can be carried out type in:
*python setup.py test* in the root directory 

Note
====

1. Sqlite3 is mandatory needs to be installed before installing gc_test. If using Ubuntu/Debian, **sudo apt install sqlite3** will do the work. More installation methods can be found at: `https://www.tutorialspoint.com/sqlite/sqlite_installation <https://www.tutorialspoint.com/sqlite/sqlite_installation>`_. If any error prompted about missing sqlite.h or python.h. That is because sqlite3 is not installed.
2. It is also recommended to run the commands in a clean virtual environment for python.
3. If there is any unexpected issue that the program cannot be installed by setuptools, the main.py is in <root>/src/gc_test and can be executed by **python main.py**, which has the same usage as gcclac.