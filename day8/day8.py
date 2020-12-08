ops_init = []
with open('day8.in') as f:
    for line in f.read().splitlines():
        ops_init.append(line.split(" ") + [False])


def check(ops):
    step = 0
    acc = 0
    while not ops[step][2]:
        val = 1
        if ops[step][0] == 'acc':
            acc += int(ops[step][1])
        elif ops[step][0] == 'jmp':
            val = int(ops[step][1])
        ops[step][2] = True
        step += val
        if step >= len(ops):
            return True, acc
    return False, acc


def fix(ops):
    for i in range(0, len(ops)):
        ops_clean = list(map(lambda o: [o[0], o[1], False], ops))
        if ops_clean[i][0] == 'nop':
            ops_clean[i][0] = 'jmp'
        elif ops_clean[i][0] == 'jmp':
            ops_clean[i][0] = 'nop'
        fixed, acc = check(ops_clean)
        if fixed:
            return acc


print(check(ops_init)[1])
print(fix(ops_init))
