def main():
    reader = open('clients.txt', 'r')

    a = 1
    for line in reader:
        print(a, '. ', line.rstrip('\n'), sep='')
        a+=1
main()    
