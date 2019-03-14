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

Exercise objective

Through the exercises in this workshop participants will read over a file containing a list of customers. They will then write functions to parse the data and calculate the distance between a mock business and each customer.

They will then identify their mock businesses closest customers and, time permitting, write the results out in geojson which they can visualize on a platform such as http://geojson.io

---

1. Python overview: qualities and conventions

    - Interpreted language
    - Interactive mode
    - Easy to learn/read syntax enforced by indentation
    - Rapid development
    - PEP 8

---

2. Installing Python and dependencies
  - Virtualenv: What it is and why it’s useful
  - What are modules and packages
  - PyPi/pip: Where you can find or distribute packages
      - installing, upgrading, searching for packages
  - Requirements.txt - creating and installing from requirements.txt

    Activity 1: Install python in a virtual environment and install dependencies using a requirements.txt file. For review we will just confirm that everyone has everything they need installed to proceed with the workshop

3. Writing functions
  a. Basic function syntax
  b. Arguments - default values
  c. Our activity will cover reading files, so we will briefly cover file i/o and using 'with' to create a context
  Activity 1: Participants will write two functions one that reads data from a csv and a second function that calculates the cartesian distance between two pairs of coordinates

4. Data Structures and Iterating
  a. Strings and string formatting
  b. Tuples, Lists, Sets, Dictionaries
  c. List comprehensions
  d. Generators
  e. Decorators
  Activity 1: Participants will read over a text file and parse each record into a dictionary.
  Activity 2: Participants will write a decorator for their distance function that will return a dictionary with the start and end coordinates, and distance value
  Activity 3: Participants will use a list comprehension to filter their data by a given distance.
