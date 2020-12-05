def split(input, c, rows):
    if len(rows) == 1:
        return rows[0] * 8 + split(input, c, list(range(0, 8))) if input[c - 1] in ["F", "B"] else rows[0]
    return split(input, c + 1, rows[:len(rows) // 2]) if input[c] in ["F", "L"] else split(input, c + 1, rows[len(rows) // 2:])


def start_rec(input):
    return split(input, 0, list(range(0, 128)))


with open("day5.in") as f:
    records = f.read().splitlines()
ids = sorted(list(map(start_rec, records)))
print(max(ids))
print([i for i in range(min(ids), max(ids) + 1) if i not in ids][0])
