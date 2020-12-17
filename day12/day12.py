import math

with open('day12.in') as f:
    directions = [[l[:1], int(l[1:])] for l in f.read().splitlines()]

face = "E"
compass = {"N": [0, 1], "E": [1, 0], "S": [0, -1], "W": [-1, 0]}
coords = [0, 0]

# part 1
for d, unit in directions:
    if d in compass.keys():
        coords = [c + compass[d][i] * unit for i, c in enumerate(coords)]
    elif d in "LR":
        face = list(compass.keys())[(list(compass.keys()).index(face) + (unit // 90 if d == "R" else -1 * unit // 90)) % 4]
    else:
        coords = [c + compass[face][i] * unit for i, c in enumerate(coords)]

print(sum(list(map(abs, coords))))

# part 2
waypoint = [10, 1]
ship = [0, 0]
face = "E"

for d, unit in directions:
    if d in compass.keys():
        waypoint = [c + compass[d][i] * unit for i, c in enumerate(waypoint)]
    elif d in "LR":
        rads = math.radians(unit) if d == "L" else -math.radians(unit)
        waypoint = [waypoint[0] * math.cos(rads) - waypoint[1] * math.sin(rads), waypoint[0] * math.sin(rads) + waypoint[1] * math.cos(rads)]
    else:
        ship = [c + waypoint[i] * unit for i, c in enumerate(ship)]

print(sum(list(map(abs, ship))))
