numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = 2

for i in numbers:
    count = 0
    if i == 1:
        continue
    for j in range(len(numbers)):
        if i % numbers[j] == 0:
            count += 1
            if count > is_prime:
                not_primes.append(i)
                break
    if count == is_prime:
        primes.append(i)

print(primes)
print(not_primes)






