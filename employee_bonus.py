import csv

def main():
    infile = open('employeepay.csv', 'r')

    csvfile = csv.reader(infile, delimiter=',')

    next(csvfile)

    for record in csvfile:
        #print('ID:', record[0], 'Name:', record[1], record[2], 'Salary:', record[3], 'Bonus:', record[4])
        print('Employee ID:', record[0])
        print('Employee Name:', record[1], record[2])
        bonus_amt = float(record[3]) * float(record[4])
        total_salary = float(record[3]) + bonus_amt
        print('Total Salary:', total_salary)
        print()
        input('Press enter for next employee.')
        print()

main()