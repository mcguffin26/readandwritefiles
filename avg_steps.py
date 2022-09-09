from calendar import month
import csv

def main():
    infile = open('steps.csv', 'r')

    b = 0
    running_total = 0.0
    day_counter = 0
    month_counter = 1
    element_count = 0
    avg = [0] * 12
    months = ['a'] * 12 
    reader = csv.reader(infile, delimiter=',')
    next(reader)
    
    months[0] = 'January'
    months[1] = 'February'
    months[2] = 'March'
    months[3] = 'April'
    months[4] = 'May'
    months[5] = 'June'
    months[6] = 'July'
    months[7] = 'August'
    months[8] = 'September'
    months[9] = 'October'
    months[10] = 'November'
    months[11] = 'December'


    #need to fix the day/month counter. december doesnt register, every month except january is off. 

    for record in reader:
        if int(record[0]) == month_counter:
            running_total += float(record[1])
            day_counter +=1
        else:
            #print(running_total)
            print(day_counter)
            print(month_counter)
            month_avg = running_total / day_counter
            # print(month_avg)
            avg[element_count] = format(month_avg, '.2f')
            day_counter = 1
            running_total = 0
            month_avg = 0
            month_counter += 1
            element_count += 1

    steps_data = [
        ['January', avg[0]],
        ['February', avg[1]],
        ['March', avg[2]],
        ['April', avg[3]],
        ['May', avg[4]],
        ['June', avg[5]],
        ['July', avg[6]],
        ['August', avg[7]],
        ['September', avg[8]],
        ['October', avg[9]],
        ['November', avg[10]],
        ['December', avg[11]],
    ]
    with open('avg_steps.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(steps_data)
    # for record in avg:
    #     outfile.write(avg[0])
    #     outfile.write(avg[1])
    #     outfile.write(avg[2])
    #     outfile.write(avg[3])
    #     outfile.write(avg[4])
    #     outfile.write(avg[5])
    #     outfile.write(avg[6])
    #     outfile.write(avg[7])
    #     outfile.write(avg[9])
    #     outfile.write(avg[9])
    #     outfile.write(avg[10])
    #     outfile.write(avg[11])
   
    print(avg)

main()