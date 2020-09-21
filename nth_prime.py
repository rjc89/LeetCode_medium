def nth_prime(n):
    '''find the nth prime number'''
    primes = [2]
    next_number = 3
    while len(primes) < n:
        for i in primes:
            if next_number % i == 0:
                break
        else:
            primes.append(next_number)
        next_number += 2
    return primes[-1]

print(nth_prime(100))