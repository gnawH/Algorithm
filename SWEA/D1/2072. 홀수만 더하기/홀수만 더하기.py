T = int(input())

for test_case in range(1, T + 1):
    result = 0
    numbers = list(map(int, input( ).split( )))
    for num in numbers:
        if num % 2 != 0:
            result += num
    print(f'#{test_case} {result}')