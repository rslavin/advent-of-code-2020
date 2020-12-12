from copy import deepcopy

with open('day11.in') as f:
    rows = list(map(lambda r: [c for c in r], f.read().splitlines()))


def check(part=1):
    global rows
    copy = deepcopy(rows)
    rx = len(copy)
    ry = len(copy[0])
    updated = False
    for row in range(rx):
        for col in range(ry):
            if copy[row][col] == ".":
                continue
            sitting_near = 0
            for subrow in [-1, 0, 1]:
                for subcol in [-1, 0, 1]:
                    if not (subcol == 0 and subrow == 0):
                        radius_mult = 1
                        while 0 <= (row + subrow * radius_mult) < rx and 0 <= (col + subcol * radius_mult) < ry:
                            if radius_mult > 1 and part == 1:
                                break
                            candidate = rows[row + subrow * radius_mult][col + subcol * radius_mult]
                            if candidate == "#":
                                sitting_near += 1
                            if candidate != ".":
                                break
                            radius_mult += 1
            if rows[row][col] == "L" and not sitting_near:
                copy[row][col] = "#"
                updated = True
            if rows[row][col] == "#" and sitting_near >= (4 if part == 1 else 5):
                copy[row][col] = "L"
                updated = True
    rows = deepcopy(copy)
    return updated


while True:
    if not check(1):
        break
print(sum(list(map(lambda l: l.count("#"), rows))))

