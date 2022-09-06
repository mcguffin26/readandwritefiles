from calendar import month
import csv

def main():
    infile = open('steps.csv', 'r')
    outfile = open('avg_steps.csv', 'w')

    running_total = 0.0
    day_counter = 0
    month_counter = 1
    a = 0
    avg = [[0, 0]] * 12
    reader = csv.reader(infile, delimiter=',')
    next(reader)
    
    #if statement is working, need to clean up the logic in the else block
    #day counter only works on the first month, the rest of the months are less by one day 

    for record in reader:
        if int(record[0]) == month_counter:
            running_total += float(record[1])
            day_counter +=1
        else:
            #print(running_total)
            print(day_counter)
            month_avg = running_total / day_counter
            print(month_avg)
            avg[a][1] = month_avg
            day_counter = 0
            month_counter += 1
            running_total = 0
            month_avg = 0
            a += 1
    print(avg)
            
main()