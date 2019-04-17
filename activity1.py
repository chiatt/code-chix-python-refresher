import folium
import functools
import json
import logging
from haversine import haversine

path = '/Users/cyrus/Documents/projects/codechix/code-chix-py-deck/customers.txt'

with open(path, 'r') as f:
    lines = f.readlines()
    header = lines[0].strip().split('|')
    records = [line.strip().split('|') for line in lines[1:]]

res = [dict(zip(header, record)) for record in records]

print(res[0])
