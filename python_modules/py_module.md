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


### 1. What is a module ?

A module allows us to organize Python code in a systematic manner. It can be considered as a file consisting of Python code. A module can define functions, classes and variables.Therefore, in order to write a longer program, we might consider switching to a text editor to prepare an input for the interpreter and running it with that file as an input instead. This is known as writing a `script`.


To support this, Python has a way to put a code definition in a file and use them in another script or directly in an interactive instance of the interpreter. Such a file is called a `module`;

**Note**: When we import the module named `math_operations`, the interpreter first searches for a built-in module with that name. If not found, it then searches for a file named `math_operations`.py in a list of directories given by the variables system path.
Apart from this, Python has a large set of built-in modules known as the Python Standard Library.


### 2. Create some functions as example to practice module import.
Now let's create a new python file called `math_operations.py` and let's write some basic functions to practice the import module.
The file math_operations.py in the modules directory.


### 3. Importing file in other script.
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



### 4. Python Standard Library.
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

### 5. List of some base functionalitiy

In addition to this, there are various other built-in modules in Python. We list some of them below based on their functionality.
1. Text Processing : string, readline, re, etc.
2.  Data Types : datetime, calendar, array, copy, pprint, etc. 
3. Mathematical : numbers, math, random, statistics, etc. 
4. Files and Directories : pathlib, stat, glob, shutil, filinput etc. 
5. Data Persistence: pickle, dbm, sqlite3, etc.
6. Compression and Archiving: gzip, bz2, zipfile, tarfile, etc.


### 6. Packages in python.
Packages can be considered as a collection of modules. It is a way of struc- turing Python’s module namespace by using "dotted module names". A package is basically a directory with Python files and a file with the name `__init__.py`. This means that every directory inside of the Python path, which contains a file named `__init__.py`, will be treated as a package by Python.

For example, the module name matplotlib.pyplot designates a submodule named pyplot in a package named matplotlib.

**Creating Package**
Let’s create a package named my_package that will contain two modules first_file and second_file. To create this module follow the below steps – 

1. Create a folder named my_package.
2. Inside this folder create an empty Python file i.e. `__init__.py`
3. Then create two modules first_file and second_file in this folder.

**The Structure of the Package**
```
my_package
    --- __init__.py

    --- first_file.py

    --- second_file.py
```

**The __init__.py**
__init__.py helps the Python interpreter to recognise the folder as package. It also specifies the resources to be imported from the modules.

```python
from .first_file import addition
from .second_file import factorial
```


**Importing specific function from a module**

```python
from my_package.first_file import addition
from my_package.second_file import factorial
```

### 7. External Libraries.
One of the great things about using Python is the number of fantastic code libraries (apart from the Python Standard Library) which are readily available for a wide variety of domains that can save much coding or make a particular task much easier to accomplish.

Before we can use such external libraries, we need to install them. To be able to install our prefered packages we first need to install a package installer, in this case we will be using `pip`.

**Installing prefered installer program (pip)**
We can install a pip via the command line by using the curl command, which downloads the pip installation perl script.
`curl -O https://bootstrap.pypa.io/get-pip.py`

Once it is downloaded, we need to execute it in the command prompt with the Python interpreter.
`python get-pip.py`


For Mac and Linux distribution due to permis- sion issues (most likely because Python does not have permission to update certain directories on the file system.we may need to run following command.
`sudo python get-pip.py`


With that out of the way, Let’s install some external libraries;

```python
# Installing the Numpy Library
pip install numpy

# Installing the requests Library
pip install requests

# Installing the matplotlib Library
pip install matplotlib
```

we can as well install a specific versions ;

```python
# Installing specific versions
pip install <LibraryName> == 1.10

# Installing a version greater than a specific number
pip install <LibraryName>  >= 3.7

```

### 8. Most popular python library.
Listed below are some of the most popular libraries used in different do- mains:

- Data Science
<font color="green">NumPy, pandas, SciPy, etc</font>
- Graphics
<font color="green">matplotlib, plotly, seaborn, bokeh, etc.</font>
- Statistics
<font color="green">statsmodels</font>
- Machine Learning
<font color="green">SciKit-Learn, Keras, TensorFlow, Theano, etc.</font>
- Web Scraping 
<font color="green">Scrapy, BeautifulSoup</font>
- Web Developer
<font color="green">Django, web2py, Flask, Pyramid, etc.</font>


### 9. Practicing how to importing Modules in various ways.

**Importing Python Modules**

We can import any module, either internal or external into our code using the import statement, in this less we will take a look at **internal modules**. Take a look at below example:

```python
# Importing an internal module
import math
```

The above example will import all definitions within the imported library. We can use these definitions using . (dot operator). For example,


**Importing an internal module**
```python
# Importing an internal module
import math

# Accessing the 'pi' attribute of the 'math' module
math.pi

# Accessing the 'floor' method from the 'math'
math.floor(10.8)
     

# output = 3.141592653589793
# output = 10

```

**We can also alias a library name while importing it with the help of the as keyword.**
```python
# Aliasing math as 'm'
import math as m

# Accessing the 'pi' attribute of the 'math' module
print(m.pi)

# Accessing the 'floor' method from the 'math'
print(m.floor(10.8))

# Accessing the 'e' attribute from the 'math'
print(m.e)

```

**Selective imports**
The other way to import a definition/module is to import all definitions in that particular module or all modules in the particular package. We can do so by using from keyword.
```python
# Import all definitions of math module
from math import *

# Accessing the 'pi' attribute of the 'math' module
print(pi)

# Accessing the 'floor' method from the 'math'
print(floor(10.8))

# Accessing the 'e' method from the 'math'
print(e)
```

**We can have selective import by implorting only one or more**
```python
# Import all definitions of math module
from math import pi, floor, e

# Accessing the 'pi' attribute of the 'math' module
print(pi)

# Accessing the 'floor' method from the 'math'
print(floor(10.8))

# Accessing the 'e' method from the 'math'
print(e)
```

**In a case where a specific method was not added but called,it will result to an error**
```python
# Import all definitions of math module
from math import pi, floor, e

# We get an Error as the ceil is not imported from math module
print(ceil(10.2))
Traceback (most recent call last):
    File "<ipython-input-33>", line 1, in <module>
    ceil(10.2)
    NameError: name 'ceil' is not defined

```

**dir`()` function**
We can use the built-in function dir() to find which names a module defines. It returns a sorted list of strings.

```python
import random 

# Finding the names that the module defines
print(dir(random))


# Another example 

import math 

print(dir(math))

```