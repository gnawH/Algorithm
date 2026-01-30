number = set(i for i in range(1, 10001))

for num in range(1, 10001):
    sum = num
    for i in str(num):
        sum += int(i)

    number.discard(sum)

for n in number:
    print(n)