import folium
import functools
import json
import logging
import os
from haversine import haversine

path = os.path.join(os.getcwd(), 'data', 'customers.txt')

with open(path, 'r') as f:
    lines = f.readlines()
    header = lines[0].strip().split('|')
    records = [line.strip().split('|') for line in lines[1:]]

res = [dict(zip(header, record)) for record in records]

print(res[0])
