gen = (1 for _ in range (100_000_000_000))

while True:
    try:
        my_value = gen.next()
        print(my_value)
    except:
        break

for my_value in gen:
    print(my_value)