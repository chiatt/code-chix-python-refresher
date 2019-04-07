import random, csv

def read_customer_data(path):
    customers = []
    with open(path, 'r') as f:
        customer_records = csv.DictReader(f, delimiter='|')
        for customer in customer_records:
            customer['easting'] = random.uniform(-122.112007, -122.056732)
            customer['northing'] = random.uniform(37.367974, 37.424979)
            customer['petcount'] = random.randrange(0, 6)
            customers.append(customer)
    return customers


customers = read_customer_data('/Users/cyrus/Documents/projects/codechix/code-chix-py-deck/Untitled')

with open('/Users/cyrus/Documents/projects/codechix/code-chix-py-deck/customers2.txt', 'w') as f:
    f.write('name|easting|northing|petcount\n')
    for customer in customers:
        rec = ('{0}|{1}|{2}|{3}\n').format(customer['name'],
            customer['easting'],
            customer['northing'],
            customer['petcount'])
        f.write(rec)
