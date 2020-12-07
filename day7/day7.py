import re

parents = dict()


def get_parents(color, holds):
    for p, c in parents.items():
        for i, b in c:
            if b == color:
                holds.add(p)
                get_parents(p, holds)
    return holds


def get_children(color):
    total = 0
    for c in parents[color]:
        total += int(c[0]) + int(c[0]) * get_children(c[1])
    return total


with open('day7.in') as f:
    for line in f.read().splitlines():
        parents[re.search(r"^(.*?) bags", line)[1]] = re.findall(r"(\d+) ([^ ]+ [^ ]+) bags?", line)

print(len(get_parents("shiny gold", set())))
print(get_children("shiny gold"))
