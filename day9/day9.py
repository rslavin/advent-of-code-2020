from itertools import permutations


def find_invalid():
    for i in range(25, len(numbers)):
        if not [pair for pair in permutations(numbers[i - 25:i], 2) if sum(pair) == numbers[i]]:
            return numbers[i]


def find_sequence(total):
    for i, n in enumerate(numbers):
        for j, m in enumerate(numbers[i:]):
            if sum(numbers[i:j]) == total:
                return min(numbers[i:j]) + max(numbers[i:j])


with open('day9.in') as f:
    numbers = list(map(int, f.read().splitlines()))

invalid = find_invalid()
print(invalid)
print(find_sequence(invalid))
