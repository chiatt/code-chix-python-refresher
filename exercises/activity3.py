import folium
import functools
import json
import logging
import os
from haversine import haversine

def calc_distance(store_location, customer, units):
    cust_y, cust_x = customer['northing'], customer['easting']
    distance = haversine(store_location, (cust_y, cust_x), unit=units)
    customer['distance'] = distance
    return customer


def format_num(val):
    try:
        return float(val)
    except ValueError as e:
        return val


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


def main():
    path = os.path.join(os.getcwd(), 'data', 'customers.txt')
    records = parse_csv(path)
    store_location = ([37.385, -122.089])
    customer_location = {'easting': -122.5, 'northing': 37.56}
    units = 'km'
    dist = calc_distance(store_location=store_location, customer=customer_location, units='km')
    print(dist)
    print(records)

if __name__ == '__main__':
    main()
