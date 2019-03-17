# A Python Refresher

---

## Just a little about me...

![](assets/img/board-measurements.jpg)

---
@title[Customize Slide Layout]

@snap[west span-50]
## This is a presentation
@snapend

---

## Workshop objectives

Through the exercises in this workshop participants will read over a file containing a list of customers. They will then write functions to parse the data and calculate the distance between a mock business and each customer.

They will then identify their mock businesses closest customers and, time permitting, write the results out in geojson which they can visualize on a platform such as http://geojson.io

---

## Python overview: qualities and conventions

    - Interpreted language
    - Interactive mode
    - Easy to learn/read syntax enforced by indentation
    - Rapid development
    - PEP 8

---

## Installing Python and dependencies

  - Virtualenv: What it is and why it’s useful
  - What are modules and packages
  - PyPi/pip: Where you can find or distribute packages
      - installing, upgrading, searching for packages
  - Requirements.txt - creating and installing from requirements.txt

    Activity 1: Install python in a virtual environment and install dependencies using a requirements.txt file. For review we will just confirm that everyone has everything they need installed to proceed with the workshop

---

## Writing functions

  - Basic function syntax
  - Arguments - default values
  - Our activity will cover reading files, so we will briefly
   cover file i/o and using 'with' to create a context
  Activity 1: Participants will write two functions one that reads data from a csv and a second function that calculates the cartesian distance between two pairs of coordinates

---

## Data Structures and Iterating

  - Strings and string formatting
  - Tuples, Lists, Sets, Dictionaries
  - List comprehensions
  - Generators
  - Decorators

---

## Activity 1:

Participants will read over a text file and parse each record into a dictionary.

---

## Activity 2:

Participants will write a decorator for their distance function that will return a dictionary with the start and end coordinates, and distance value

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
@[4]
@[5-7]

---

## Activity 3:

Participants will use a list comprehension to filter their data by a given distance.
