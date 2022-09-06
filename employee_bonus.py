import csv

def main():
    infile = open('employeepay.csv', 'r')

    csvfile = csv.reader(infile, delimiter=',')

    next(csvfile)

    for record in csvfile:
        print('Employee ID:  ', record[0])
        print('Employee Name:', record[1], record[2])
        bonus_amt = float(record[3]) * float(record[4])
        total_salary = float(record[3]) + bonus_amt
        print('Total Pay:     ', '$', format(total_salary, ',.2f'), sep='')
        print()
        input('Press enter for next employee.')
        print()

main()