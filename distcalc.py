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

distance_no_dec = calc_distance_no_decorator(
    start={'x': 5, 'y': 10},
    end={'x': 2, 'y': 7})

print(distance)
print(distance_no_dec)
