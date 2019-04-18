"""
Activity 1a: Read over a text file and parse each record into a dictionary

1. Open customers.txt and read the file using `readlines()`
2. Assign the first line to a variable called 'header'
3. Using a list comprehension insert the remaining lines into a new list called 'records'
"""

path = '/Users/cyrus/Documents/projects/codechix/code-chix-py-deck/customers.txt'

with open(path, 'r') as f:
    lines = f.readlines()
    header = lines[0]
    records = [line for line in lines[1:]]

print(records[0:3])

"""
### Activity 1b: Read over a text file and parse each record into a dictionary

1. Use `.strip().split()` to split your header into a list
2. Modify your list comprehension to split each line into a list with `.strip().split()`
3. At this point you should have a list of lists.
4. Write a second list comprehension that zips the header with each record in your 'records list'
"""

path = '/Users/cyrus/Documents/projects/codechix/code-chix-py-deck/customers.txt'

with open(path, 'r') as f:
    lines = f.readlines()
    header = lines[0].strip().split('|')
    records = [line.strip().split('|') for line in lines[1:]]

res = [dict(zip(header, record)) for record in records]

"""
### Activity 2:

Write two functions  

1. One called 'parse_csv' to read customers.txt and return a list of dictionaries.
    It should take a path and a delimeter as arguments.

2. One to that takes a string as an argument. If the string can be converted to
    float, the function should return a float, otherwise is should just return
    the string.
"""

path = '/Users/cyrus/Documents/projects/codechix/code-chix-py-deck/customers.txt'


def parse_csv(path, delimiter='|'):
    with open(path, 'r') as f:
        lines = f.readlines()
        header = lines[0].strip().split(delimiter)
        records = [
            line.strip().split(delimiter) for line in lines[1:]
            ]

    res = [dict(zip(header, record)) for record in records]

    return res


def format_num(val):
    try:
        return float(val)
    except ValueError as e:
        return val


"""
Activity 3
1. Update your parse_csv function to return a generator expression rather than
    a list.
2. Write a function that calculates the distance between a store location and a
    customer
"""

from haversine import haversine

store_location = ([37.385, -122.089])
customer_location = {'easting': -122.5, 'northing': 37.56}
units = 'km'


def calc_distance(store_location, customer, units):
    cust_y, cust_x = customer['northing'], customer['easting']
    distance = haversine(store_location, (cust_y, cust_x), unit=units)
    customer['distance'] = distance
    return customer


def parse_csv(path, delimiter='|'):
    with open(path, 'r') as f:
        lines = f.readlines()
        header = lines[0].strip().split(delimiter)
        records = (
            line.strip().split(delimiter) for line in lines[1:]
        )

    res = (
        dict(zip(header, [format_num(r) for r in record])) for record in records
        )
    return res


records = parse_csv(path)

"""
Activity 4
1. Activity: Write a decorator that truncates a string down to 6 letters
"""

import functools


def abbreviate(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        get_string_res = func(*args, **kwargs)
        return '{0} ...'.format(get_string_res[0:6])
    return wrapper


@abbreviate
def get_string(some_string):
    return some_string
