import folium
import functools
import math
import csv

# read create location
# read file/create customers
# calculate distance
# create map
def using_args(foo, *args):
    print('foo:', foo)
    print('*args:', args)

def using_kwargs(foo, **kwargs):
    print('foo:', foo)
    print('**kwargs:', kwargs)

def using_args_and_kwargs(foo, *args, **kwargs):
    print('foo:', foo)
    print('*args:', args)
    print('**kwargs:', kwargs)

def read_customer_data(path):
    with open(path, 'r') as f:
        customers = csv.reader(f, delimiter='|')
        for customer in customers:
            print(customer)

def calc_distance_no_decorator(start=0, end=0):
    res = math.sqrt(((start['x']-end['x'])**2) + ((start['y']-end['y'])**2))
    return res

def make_geojson(func):
    @functools.wraps(func)
    def wrapper_convert_to_json(**kwargs):
        print(kwargs)
        kwargs['distance'] = func(**kwargs)
        return kwargs
    return wrapper_convert_to_json

@make_geojson
def calc_distance(start, end):
    res = math.sqrt(((start['x']-end['x'])**2) + ((start['y']-end['y'])**2))
    return res

def map_results(features=[]):
    gj = """
        {
          "type": "FeatureCollection",
          "features": [
            {
              "type": "Feature",
              "properties": {},
              "geometry": {
                "type": "Point",
                "coordinates": [
                  -121.80816650390625,
                  36.41465185677695
                ]
              }
            }
          ]
        }
        """

    m = folium.Map(
        location=[36.41465185677695, -121.8],
        tiles='OpenStreetMap',
        zoom_start=16
    )

    folium.GeoJson(
        gj,
        name='geojson'
    ).add_to(m)

    folium.LayerControl().add_to(m)
    m.save('index.html')

def main():
    using_args('inventory', 'birds', 'hamsters')
    using_kwargs('inventory', birds=10, hamsters=5)
    using_args_and_kwargs('inventory', 'cats', 'dogs', birds=10, hamsters=5)
    read_customer_data('/Users/cyrus/Documents/projects/codechix/code-chix-py-deck/customers.txt')
    distance = calc_distance(start={'x': 5, 'y': 10}, end={'x': 2, 'y': 7})
    distance_no_dec = calc_distance_no_decorator(start={'x': 5, 'y': 10}, end={'x': 2, 'y': 7})

    print(distance)
    print(distance_no_dec)
    map_results()

if __name__ == '__main__':
    main()
