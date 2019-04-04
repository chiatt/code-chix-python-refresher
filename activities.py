

Structures and Iterating
1) Participants will read over a text file and parse each record into a dictionary

1. create an empty list called customers
2. open customers.txt
3. read the file using file.readlines()
4. parse each line into a list using str.split() and append it to your customer list
5. at this point you should have a list of lists.

```
    [['linda', '122.12', '37.59', '2'],
     ['ralph', '122.09', '37.50', '4'],
     ['kieth', '122.20', '37.51', '2'],
     ['cindy', '122.16', '37.57', '1'],
     ['aimee', '122.11', '37.53', '3']]
```

6. use a comprehension to convert the list into a list of dictionaries
```
    [{'name': 'linda', 'easting': '122.12'},
     {'name': 'ralph', 'easting': '122.09'},
     {'name': 'kieth', 'easting': '122.20'},
     {'name': 'cindy', 'easting': '122.16'},
     {'name': 'aimee', 'easting': '122.11'}]
 ```

Writing functions
1) Participants will write two functions one that reads data from a csv and a second function that calculates the cartesian distance between two pairs of coordinates

Advanced Functions
1) Participants will write a decorator for their distance function that will return a dictionary with the start and end coordinates, and distance value
2) Participants will use a list comprehension to filter their data by a given distance.
