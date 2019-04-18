import folium
import functools
import json
import logging
import os
from haversine import haversine

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


def main():
    path = os.path.join(os.getcwd(), 'data', 'customers.txt')
    records = parse_csv(path)
    print(records[0])

if __name__ == '__main__':
    main()
