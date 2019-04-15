# Part 3

path = '/Users/cyrus/Documents/projects/codechix/code-chix-py-deck/customers.txt'

with open(path, 'r') as f:
    customer_records = f.readlines()
    header = customer_records[0].strip().split('|')
    customers = [
        customer.strip().split('|') for customer in customer_records[1:]
        ]

customer_records = [
    dict(zip(header, customer)) for customer in customers
    ]

for rec in customer_records[0:1]:
    print(rec)

# Part 4

def parse_csv(path, delimiter='|'):
    with open(path, 'r') as f:
        lines = f.readlines()
        header = lines[0].strip().split(delimiter)
        records = [
            line.strip().split('|') for line in lines[1:]
            ]

    res = [
        dict(zip(header, record)) for record in records
        ]
    return customers

records = parse_csv(path)

print('parsing customer records')
for rec in customer_records[0:2]:
    print(rec)

#-------------------------------

def make_geojson(func):
    @functools.wraps(func)
    def wrapper_convert_to_json(**kwargs):
        feature = {
          "type": "Feature",
          "properties": {},
          "geometry": {
            "type": "Point",
            "coordinates": [
                float(kwargs['customer']['easting']),
                float(kwargs['customer']['northing']),
            ]
          }
        }
        feature['properties'] = kwargs['customer']
        feature['properties']['distance'] = func(**kwargs)
        return feature
    return wrapper_convert_to_json

@make_geojson
def calc_distance(store, customer):
    x1, x2 = float(store['easting']), float(customer['easting'])
    y1, y2 = float(store['northing']), float(customer['northing'])
    res = math.sqrt(
        ((x1-x2)**2) + ((y1-y2)**2)
    )
    return res

features = []
for rec in records:
    f = calc_distance(store={'easting': -122.5, 'northing': 37.51}, customer=rec)
    features.append(f)
