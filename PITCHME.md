## A Python Refresher

---

### Just a little about me...

![](assets/img/board-measurements.jpg)

---

### Workshop outline

- Python overview
- installation and dependencies
- data structures
- functions
- generators and comprehensions
- decorators

- Activities: Map some customer data for a mock business

---

## Part I: Python Overview

- Interpreted language
- Interactive mode
- Easy to learn/read syntax enforced by indentation
- Rapid development
- PEP 8

---

## Part II: Installation and dependencies

- Virtualenv
- PyPi and pip
- requirements

---

#### Virtualenv

- Allows you to have multiple installations of Python
- Useful for projects with different versions of the
same dependency.
- Node does this differently with a global installation and dependencies
installed in each project directory.

---

#### requirements.txt

folium==0.8.3
ipdb==0.12

---

#### Installing with requirements

##### unix/linux

~~~~{.bash}
$ virtualenv env
$ source env/bin/activate
(env)$ pip install -r requirements.txt
~~~~

#### Windows

~~~~{.bash}
> virtualenv env
> env\Scripts\activate
(env) > pip install -r requirements.txt
~~~~

---

Activity:

- create a virtualenv
- install dependencies from requirements.txt

---

## Part III: Data structures and Iteration

---

#### data structures

- Tuples
- Lists
- Dictionaries
- Sets

---

#### data structures - tuples

- immutable
- store heterogeneous object types
- enclosed in ()
- trailing comma for 1 item tuples

----

#### data structures - lists

- mutable
- store heterogeneous object types
- enclosed in []
- trailing comma isn't needed
- zip

----

#### data structures - dictionaries

- store heterogeneous object types
- ordered in Python 3, unordered in Python 2
- zip dict

----

#### data structures - sets

----

#### iteratation

- for
- enumerate
- iterating over dictionaries

---

#### list comprehensions

---

#### set comprehensions

---

## Part VI: Functions

  - basic function syntax
  - arguments - positional and named
  - args and kwargs
  - main
  - Our activity will cover reading files, so we will briefly
   cover file i/o and using 'with' to create a context
  Activity 1: Participants will write two functions one that reads data from a csv and a second function that calculates the cartesian distance between two pairs of coordinates

---

#### A function

~~~~{.python}
def add_numbers(x, y):
    return x + y
~~~~

~~~~{.python}
>>> add_numbers(22, 8)
30
~~~~

---

#### Positional and Named Arguments

~~~~{.python}
def add_numbers(x, y="7"):
    pass

def add_numbers(x="2", y="7"):
    pass

# You can't do:
def add_numbers(x="2", y):
    pass
~~~~

---


#### Argument Lists and Keyword Arguments

~~~~{.python}
def add_numbers(*args, **kwargs):
    pass

def add_numbers(*cats, **dogs):
    pass
~~~~

---

#### Argument List Example

~~~~{.python}
def using_args(foo, *args):
    print('foo:', foo)
    print('*args:', args)
~~~~

~~~~{.bash}
>>> using_args('inventory', 'birds', 'hamsters')

foo: inventory
*args: ('birds', 'hamsters')
~~~~

---
#### Keyword Argument Example

~~~~{.python}
def using_kwargs(foo, **kwargs):
    print('foo:', foo)
    print('**kwargs:', kwargs)
~~~~

~~~~{.bash}
>>> using_kwargs('inventory', birds=10, hamsters=5)
foo: inventory
**kwargs: {'birds': 10, 'hamsters': 5}
~~~~

---
#### Argument Lists and Keywords Example

~~~~{.python}
def using_args_and_kwargs(foo, *args, **kwargs):
    print('foo:', foo)
    print('*args:', args)
    print('**kwargs:', kwargs)
~~~~

~~~~{.bash}
>>> using_args_and_kwargs('inventory', 'cats', 'dogs', birds=10, hamsters=5)
foo: inventory
*args: ('cats', 'dogs')
**kwargs: {'birds': 10, 'hamsters': 5}
~~~~

---

#### Main

~~~~{.python}
def add_numbers(x, y):
return x + y

def main():
add_numbers()

if __name__ == "__main__":
main()
~~~~

---

## Part V: Functions - Generators and Decorators

---

## Activity 1:

Participants will read over a text file and parse each record into a dictionary.

---

#### Decorators

---

~~~~{.python}
import functools
import math

def make_geojson(func):
    @functools.wraps(func)
    def wrapper_convert_to_json(**kwargs):
        kwargs['distance'] = func(**kwargs)
        return kwargs
    return wrapper_convert_to_json

@make_geojson
def calc_distance(start, end):
    res = math.sqrt(((start['x']-end['x'])**2) + ((start['y']-end['y'])**2))
    return res

def calc_distance_no_decorator(start, end):
    res = math.sqrt(((start['x']-end['x'])**2) + ((start['y']-end['y'])**2))
    return res

distance = calc_distance(start={'x': 5, 'y': 10}, end={'x': 2, 'y': 7})
distance_no_dec = calc_distance_no_decorator(start={'x': 5, 'y': 10}, end={'x': 2, 'y': 7})

print distance
print distance_no_dec
~~~~

@[1]
@[3-9]
@[10-14]
@[15-18]
@[20]
@[21]

---

## Activity 2:

Participants will write a decorator for their distance function that will return a dictionary with the start and end coordinates, and distance value

---
