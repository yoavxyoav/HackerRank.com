import sys

data = [] 
for line in sys.stdin:
    data.append(list(map(lambda x: int(x), line.split(" "))))

values = data[1]
weights = data[2]

def weighted_mean(values, weights):
    return round(sum([x*y for x, y in zip(values, weights)]) / sum(weights), 1)

print(weighted_mean(values, weights))
