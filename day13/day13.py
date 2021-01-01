import re

with open('day13.in') as f:
    depart = int(f.readline().rstrip())
    busses = re.findall(r"[^,]+", f.readline())
    busses_nox = [(i, int(busses[i])) for i in range(len(busses)) if busses[i] != 'x']

stops = {b[1]: i for b in busses_nox for i in range(depart, depart + b[1]) if not i % b[1]}
earliest = min(stops, key=stops.get)
print(earliest * (stops[earliest] - depart))

lcm = 1
time = busses_nox[0][1]
for i, bus in enumerate(busses_nox[1:], start=1):
    lcm *= busses_nox[i-1][1]
    while (busses_nox[i][0] + time) % bus[1]:
        time += lcm

print(time)
