## <u>MODULES IN PYTHON</u>

**What your will learn**

1. What are modules in python
2. Create some functions as example to practice module import.
3. Importing file in other script.
4. Python Standard Library
5. List of some base functionalitiy
6. Packages in python
7. External Libraries
    - Installing pip (prefered installer program)
    - Installing Libraries
        - pandas library
        - numpy library
        - requests library
    - Installing specific versions
8. Most popular python library
    - Data Science
    - Graphics
    - Statistics
    - Machine Learning
    - Web Scraping 
    - Web Developer
9. Practicing how to importing Modules in various ways.
    - import statement
    - Aliasing import statement
    - selective import
    - using the dir() function 


### What is a module ?

A module allows us to organize Python code in a systematic manner. It can be considered as a file consisting of Python code. A module can define functions, classes and variables.Therefore, in order to write a longer program, we might consider switching to a text editor to prepare an input for the interpreter and running it with that file as an input instead. This is known as writing a `script`.


To support this, Python has a way to put a code definition in a file and use them in another script or directly in an interactive instance of the interpreter. Such a file is called a `module`;

**Note**: When we import the module named `math_operations`, the interpreter first searches for a built-in module with that name. If not found, it then searches for a file named `math_operations`.py in a list of directories given by the variables system path.
Apart from this, Python has a large set of built-in modules known as the Python Standard Library.


### Create some functions as example to practice module import.
Now let's create a new python file called `math_operations.py` and let's write some basic functions to practice the import module.
The file math_operations.py in the modules directory.


### Importing file in other script.
We can import a python file in other files by using the `import keyword` followed by the module name or the name of the python file that contains the functions that is to be imported.

```Python
# Import a module called math_math_operations.py

import math_operations

# calling some functions in the module math_operations
# Creating a variable called result

result = math_operations.addition(20,20)
print(result)

# Another example 

result_mult = math_operations.multiply(2, 10)
print(result_mult)

```
This is to import files in other python script ot file.



### Python Standard Library.
Python comes with a library of standard modules also referred to as the Python Standard Library1. Some modules are built into the interpreter; these modules provide access to operations that are not part of the core of the language but are either for efficiency or to provide access to tasks pertaining to the operating system.Python’s standard library is very extensive and offers a wide range of facilities.

One particular module that deserves attention is sys, which is built into every Python interpreter. This module provides access to variables used or maintained by the interpreter and to functions that interact with the inter- preter. 

```python
# Importing the sys module in python
import sys

# Returns a string containing the copyright pertaining to the Python interpreter
print(sys.copyright)

# Returns information regarding the Python interpreter
print(sys.implementation)

```

### List of some base functionalitiy

In addition to this, there are various other built-in modules in Python. We list some of them below based on their functionality.
1. Text Processing : string, readline, re, etc.
2.  Data Types : datetime, calendar, array, copy, pprint, etc. 
3. Mathematical : numbers, math, random, statistics, etc. 
4. Files and Directories : pathlib, stat, glob, shutil, filinput etc. 
5. Data Persistence: pickle, dbm, sqlite3, etc.
6. Compression and Archiving: gzip, bz2, zipfile, tarfile, etc.


### Packages in python.
Packages can be considered as a collection of modules. It is a way of struc- turing Python’s module namespace by using "dotted module names". A package is basically a directory with Python files and a file with the name `__init__.py`. This means that every directory inside of the Python path, which contains a file named `__init__.py`, will be treated as a package by Python.

For example, the module name matplotlib.pyplot designates a submodule named pyplot in a package named matplotlib.
