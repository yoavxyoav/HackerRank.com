# https://www.hackerrank.com/challenges/s10-quartiles/problem

import sys
from math import floor, ceil

data = [] 
for line in sys.stdin:
    data.append(list(map(lambda x: int(x), line.split(" "))))

n = data[0]
arr = data[1]

def quartiles(arr):

    # arr = list(set(arr))
    arr = sorted(arr)
    n = len(arr)

    median = (arr[n//2 + n%2 - 1] + arr[n//2]) / 2

    L = arr[:n//2]
    H = arr[n//2 + n%2:]

    new_n = len(L)
    q1 = (L[new_n//2 + new_n%2 - 1] + L[new_n//2]) / 2
    q3 = (H[new_n//2 + new_n%2 - 1] + H[new_n//2]) / 2

    #rounding and int/float stuff
    q1, median, q3 = map(lambda x: int(x) if (x*10%10 == 0) else x, (q1, median, q3))

    return (q1, median, q3)

q1, median, q3 = quartiles(arr)
print(q1)
print(median)
print(q3)
