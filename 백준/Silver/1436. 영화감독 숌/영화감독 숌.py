n = int(input())
count = 665
result = 0

while 1:
    count += 1
    if '666' in str(count):
        result += 1
        if result == n:
            print(count)
            break
    