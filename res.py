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
