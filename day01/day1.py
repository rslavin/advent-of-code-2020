with open('day1.in') as f:
    numbers = list(map(lambda s: int(s), f.read().splitlines()))
    print([n1 * n2 for i, n1 in enumerate(numbers) for n2 in numbers[i + 1:] if n1 + n2 == 2020][0])
    print([n1 * n2 * n3 for i, n1 in enumerate(numbers) for j, n2 in enumerate(numbers[i + 1:]) for n3 in numbers[j + 1:] if n1 + n2 + n3 == 2020][0])
