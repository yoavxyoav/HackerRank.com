# https://www.hackerrank.com/challenges/s10-interquartile-range/problem?h_r=next-challenge&h_v=zen



import sys
from math import floor, ceil
from operator import itemgetter

data = [] 
for line in sys.stdin:
    data.append(list(map(lambda x: int(x), line.split(" "))))

n = data[0]
val = data[1]
freq = data[2]



def iq_range(val, freq):
    d = {}
    for v, f in zip(val, freq):
        d[v] = f

    val = sorted(val)

    arr =  [[x]*d[x] for x in sorted(val)]

    r = []
    for l in arr:
        for i in l:
            r.append(i)

    arr = r
    n = len(arr)

    median = (arr[n//2 + n%2 - 1] + arr[n//2]) / 2

    L = arr[:n//2]a
    H = arr[n//2 + n%2:]

    new_n = len(L)
    q1 = (L[new_n//2 + new_n%2 - 1] + L[new_n//2]) / 2
    q3 = (H[new_n//2 + new_n%2 - 1] + H[new_n//2]) / 2

    #rounding and int/float stuff
    # q1, median, q3 = map(lambda x: int(x) if (x*10%10 == 0) else x, (q1, median, q3))

    interquartile_range = q3-q1

    return interquartile_range


print(iq_range(val, freq))

