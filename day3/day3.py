def count_trees(dx, dy, lines):
    x = trees = 0
    for line in lines[::dy]:
        trees += 1 if line[x % len(line)] == "#" else 0
        x += dx
    return trees


with open('day3.in') as f:
    lines = f.read().splitlines()
print(count_trees(3, 1, lines))
print(count_trees(1, 1, lines) * count_trees(3, 1, lines) *
      count_trees(5, 1, lines) * count_trees(7, 1, lines) * count_trees(1, 2, lines))
