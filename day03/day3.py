def count(dx, dy, lines):
    return len([1 for n, l in enumerate(lines[::dy]) if l[n * dx % len(l)] == "#"])


with open('day3.in') as f:
    lines = f.read().splitlines()
print(count(3, 1, lines))
print(count(1, 1, lines) * count(3, 1, lines) * count(5, 1, lines) * count(7, 1, lines) * count(1, 2, lines))
