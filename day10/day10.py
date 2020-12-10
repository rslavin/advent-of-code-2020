from collections import defaultdict

with open('day10.in') as f:
    adapters = sorted(list(map(int, f.read().splitlines())))
    adapters = [0] + adapters + [max(adapters) + 3]

diffs = defaultdict(int)
for i, a in enumerate(adapters[:-1]):
    diffs[adapters[i + 1] - a] += 1

print(diffs[1] * diffs[3])

paths = [1] + [0] * (max(adapters))
for a in adapters[1:]:
    paths[a] = sum([paths[x] for x in range(a - 3, a)])

print(paths[-1])
