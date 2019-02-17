#import array as arr
from math import log2
import sys
#merge sort implementation taken from boubakr at this stackoverflow link: https://stackoverflow.com/questions/18761766/mergesort-python
def merge_sort(sequence):
    """
    Sequence of numbers is taken as input, and is split into two halves, following which they are recursively sorted.
    """
    if len(sequence) < 2:
        return sequence

    mid = len(sequence) // 2     # note: 7//2 = 3, whereas 7/2 = 3.5

    left_sequence = merge_sort(sequence[:mid])
    right_sequence = merge_sort(sequence[mid:])

    return merge(left_sequence, right_sequence)

def merge(left, right):
    """
    Traverse both sorted sub-arrays (left and right), and populate the result array
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result

def probSort():
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
    log = log2(int(number))
    if (greedyhigh - greedylow) < (log):
        print('Using collapso masto')
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
    else:
        print('Using mergsort')
        print(merge_sort(number_array))
probSort()
