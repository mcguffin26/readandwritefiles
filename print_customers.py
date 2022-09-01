import csv

def main():
    infile = open('customers.csv', 'r')
    
    csvfile = csv.reader(infile, delimiter=',')

    next(csvfile) #skip first row in csv file 

    for record in csvfile:
        print('ID:', record[0], '\nFirst Name:', record[1], '\nLast Name:', record[2], '\nCity:', record[3], '\nCountry:', record[4], '\nPhone Number:', record[5])
        
        input()

main()