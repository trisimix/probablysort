#import array as arr
import sys
def probablySort():
    number_array = list()
    number = input("Enter the number of elements you want:")
    print ('Enter numbers in array: ')
    for i in range(int(number)):
        n = input("number :")
        number_array.append(int(n))
        print ('ARRAY: ',number_array)
    ## above line is building input array
    greedylow = sys.maxsize
    greedyhigh = -int(sys.maxsize)
    # n below
    for i in range(int(number)):
        if number_array[i] < greedylow:
            greedylow = number_array[i]
    # n below
    for i in range(int(number)):
        if number_array[i] > greedyhigh:
            greedyhigh = number_array[i]
    offset = int(greedylow * -1)
    whitelist = [None] * (greedyhigh - greedylow + 1)
    # n below
    for i in range(int(number)):
        print (number_array[i] + offset)
        whitelist[(number_array[i]) + offset] = number_array[i]
        print ('Whitelist: ',whitelist)
    unwhitelist = list()
    # m where m is the difference between lowest integer in list and highest integer in list
    for i in range(len(whitelist)):
        if whitelist[i]:
            unwhitelist.append(whitelist[i])
            print (unwhitelist)
    print(unwhitelist)
probablySort()