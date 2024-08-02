def find_pairs(n):
    pairs = []
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if n % (i + j) == 0:
                pairs.append(f'{i}{j}')
    return ''.join(pairs)


n = int(input('Введите число от 3 до 20: '))
password = find_pairs(n)
print(f'{n} - {password}')
