mem = {}

with open("day14.in") as f:
    for line in f.readlines():
        l, r = line.split(" = ")
        if l == "mask":
            ones = int(r.replace("X", "0"), base=2)
            zeroes = int(r.replace("X", "1"), base=2)
        else:
            mem[int(l[4:-1])] = int(r) & zeroes | ones

print(sum(mem.values()))


def addr_gen(address):
    if "X" in address:
        for b in "0", "1":
            for add in addr_gen(address.replace("X", b, 1)):
                yield add
    else:
        yield address


mem = {}
with open("day14.in") as f:
    for line in f.readlines():
        l, r = line.split(" = ")
        if l == "mask":
            mask = r.zfill(36).rstrip()
        else:
            address = []
            for i, b in enumerate(format(int(l[4:-1]), 'b').zfill(36)):
                if mask[i] == "1":
                    address.append("1")
                elif mask[i] == "0":
                    address.append(b)
                else:
                    address.append("X")

            for address in addr_gen("".join(address)):
                mem[int(address, base=2)] = int(r)

print(sum(mem.values()))
