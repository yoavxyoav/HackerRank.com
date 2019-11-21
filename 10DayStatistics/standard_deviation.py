# https://www.hackerrank.com/challenges/s10-standard-deviation/problem
import sys
from math import sqrt

data = [] 
for line in sys.stdin:
    data.append(list(map(lambda x: int(x), line.split(" "))))



n = data[0]
vals = data[1]

def std(arr):
    n = len(arr)
    mean = sum(arr) / n
    std = sqrt(sum([(x - mean)**2 for x in arr]) / n)
    std = round(std, 1)
    return std

print(std(vals))
