def fizzbuzz(n):
    s = ''
    for i in range(1, n, 1):
        if i % 3 == 0:
            s += 'Fizz'
        if i % 5 == 0:
            s += 'Buzz'
        elif len(s) == 0:
            print(i)
            continue
        print(i, s)
        s = ''

print(fizzbuzz(30))