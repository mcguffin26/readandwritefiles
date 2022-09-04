from calendar import c
import csv
from re import A

def main():
    
    outfile = open('customer_country.csv', 'w')
    customer_data = 'customers.csv'

    rows = []
    a = 0

    with open(customer_data, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        next(csvreader)

        for row in csvreader:
            rows.append(row)
    
    for row in rows: 
        outfile.write(rows[a][1] + ' ' + rows[a][2] + ', ' + rows[a][4] + '\n')
        a+=1

    print(outfile)
main()
