import csv

with open('sw_data.csv') as f:
    reader = csv.reader(f)        #csv.reader(f, delimiter=';')
    headers = next(reader)        #get headers in separated var
    print('Headers: ', headers)
    for row in reader:
        print(row)
		
		
		
=============================
#DictReader		
import csv

with open('sw_data.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        print(row['hostname'], row['model'])
		
		
=============================
#writer
import csv

data = [['hostname', 'vendor', 'model', 'location'],
        ['sw1', 'Cisco', '3750', 'London, Best str'],
        ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
        ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
        ['sw4', 'Cisco', '3650', 'London, Best str']]

with open('sw_data_new.csv', 'w') as f:
    writer = csv.writer(f)           # writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in data:
        writer.writerow(row)

with open('sw_data_new.csv') as f:
    print(f.read())
	
=============================
#writerows
import csv

data = [['hostname', 'vendor', 'model', 'location'],
        ['sw1', 'Cisco', '3750', 'London, Best str'],
        ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
        ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
        ['sw4', 'Cisco', '3650', 'London, Best str']]

with open('sw_data_new.csv', 'w') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(data)

with open('sw_data_new.csv') as f:
    print(f.read())
	
===============================
#DictWriter
import csv


data = [{'hostname': 'sw1',
         'location': 'London',
         'model': '3750',
         'vendor': 'Cisco'},
        {'hostname': 'sw2',
         'location': 'Liverpool',
         'model': '3850',
         'vendor': 'Cisco'},
        {'hostname': 'sw3',
         'location': 'Liverpool',
         'model': '3650',
         'vendor': 'Cisco'},
        {'hostname': 'sw4',
         'location': 'London',
         'model': '3650',
         'vendor': 'Cisco'}]

with open('csv_write_dictwriter.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=list(data[0].keys()),
                            quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for d in data:
        writer.writerow(d)