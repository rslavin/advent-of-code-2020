import re

reqs = {"byr": lambda e: 1920 <= int(e) <= 2002,
        "iyr": lambda e: 2010 <= int(e) <= 2020,
        "eyr": lambda e: 2020 <= int(e) <= 2030,
        "hgt": lambda e: hgt_validator(e),
        "hcl": lambda e: re.search(r"^#[0-9a-f]{6}$", e),
        "ecl": lambda e: re.search(r"^amb|blu|brn|gry|grn|hzl|oth$", e),
        "pid": lambda e: re.search(r"^\d{9}$", e)}


def hgt_validator(s):
    m = re.search(r"^(\d+)(..)", s)
    return m and (150 <= int(m.group(1)) <= 193 and m.group(2) == "cm" or 59 <= int(m.group(1)) <= 76 and m.group(2) == "in")


def validate(p):
    fields = dict(e.split(":") for e in re.split(r"[ \n]", p) if not e.startswith("cid"))
    return len(fields) == 7 and len({k: v for k, v in fields.items() if reqs[k](v)}) == 7


with open("day4.in") as f:
    records = f.read().split("\n\n")
print(len(list(filter(lambda p: all(e in p for e in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]), records))))
print(len(list(filter(lambda p: validate(p), records))))
