#!/bin/python3

import math
import os
import random
import re
import sys





#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a,n):
    swaps=0
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                aux = a[j]
                a[j] = a[j+1]
                a[j+1] = aux
                swaps+=1
    return a,swaps
                


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    a,swaps=countSwaps(a,n)
    print('Array is sorted in ' + str(swaps)+ ' swaps.')
    print('First Element: '+str(a[0]))
    print('Last Element: '+str(a[-1]))
