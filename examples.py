import folium
import functools
import math
import csv

## closures
def get_fn():
    x = 21
    def add_numbers(y):
        return x + y
    return add_numbers

ff = get_fn()
print(ff(2))

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

#### Generators
def create_records_generator(start, end):
    while start < end:
        start += 1
        yield start

def create_records_array(start, end):
    res = []
    while start < end:
        start += 1
        res.append(start)
    return res

generator = create_records_generator(3, 100000000)
for x in generator:
    if x % 10000000 == 0:
        print('from generator', x)

array = create_records_array(3, 100000000)
for n in array:
    if n % 10000000 == 0:
        print('from array', n)
# Generators require less memory than lists
# Then why not always use generators?
## lists should be used when you are iterating multiple times over the list (because they're cached).
## lists are needed when you need to access items out of order


def read_customer_data(path):
    with open(path, 'r') as f:
        customers = []
        customer_records = csv.DictReader(f, delimiter='|')
        for customer in customer_records:
            print(customer['easting'])
            customers.append(customer)
        print(customers)

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
