with open("day6.in") as f:
    groups = f.read().split("\n\n")

print(sum(list(map(lambda g: len(set(g.replace("\n", ""))), groups))))
print(sum(list(map(lambda a: len(set.intersection(*map(set, a))), list(map(lambda g: g.splitlines(), groups))))))
