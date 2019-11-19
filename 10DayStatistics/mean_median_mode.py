import sys

for line in sys.stdin:
    arr = list(map(lambda x: int(x), line.split(" ")))


def mean(arr):
    return sum(arr)/len(arr)

def median(arr):
    arr = sorted(arr)
    ind = len(arr) // 2
    if len(arr) % 2 == 1:
        return arr[ind]
    else:
        return (arr[ind-1] + arr[ind]) / 2

def mode(arr):
    nums = {}
    for x in arr:
        if x not in nums:
            nums[x] = 0
        else:
            nums[x] += 1
    val = max(list((nums.values())))
    if val == 0:
        return min(arr)
    else:
        vals = [x[0] for x in nums.items() if x[1] == val]
        return min(vals)


print(mean(arr))
print(median(arr))
print(mode(arr))
