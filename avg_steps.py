from calendar import month
import csv

def main():
    infile = open('steps.csv', 'r')
    outfile = open('avg_steps.csv', 'w')

    running_total = 0
    day_counter = 0
    month_counter = 1
    avg = [[0, 0]] * 12
    reader = csv.reader(infile, delimiter=',')
    next(reader)
    

    for row in reader:
        if row[month_counter] == str(1):
            day_counter +=1
            avg[month_counter][1] = running_total + row[1]
    print(avg)
            
    # for row in reader:
    #     print(row)
    #     if int(row[0]) == 1:
    #         running_total += int(row[1])
    #         avg[0] = 'January'  
    #         jan_avg = running_total/31
    #         avg[1] = jan_avg

    # running_total = 0
    # for row in reader:
    #     if int(row[0]) == 2:
    #         running_total += int(row[1])
    #         avg[2] = 'February'  
    #         feb_avg = running_total/28
    #         avg[3] = feb_avg

    # running_total = 0
    # for row in reader:
    #     if int(row[0]) == 3:
    #         running_total += int(row[1])
    #         avg[4] = 'March'  
    #         mar_avg = running_total/31
    #         avg[5] = mar_avg    
    
    # print(avg)

main()