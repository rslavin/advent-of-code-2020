import re

with open("day2.in") as f:
    lines = list(map(lambda l: re.search(r"(\d+)-(\d+) (.): (.*)", l).groups(), f.readlines()))
    print(len([1 for (min, max, c, password) in lines if int(min) <= password.count(c) <= int(max)]))
    print(len([1 for (min, max, c, password) in lines if (password[int(min) - 1] == c) ^ (password[int(max) - 1] == c)]))
