numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for n in numbers:
    if n==1:
        continue

        for i in (2,16):
            if i % n  == 0:
                is_primes = 0
                break
                if is_primes:
                    primes.append(n)
                    print('Простые числа', primes)
                else:
                    not_primes.append(n)
                    print('Составные числа', not_primes)
                    # Не понимаю,почему ничего не выводит




