T = int(input())

for test_case in range(1, T+1):
    case_numbers = list(map(int, input().split()))
    float_answer = (sum(case_numbers) - (max(case_numbers) + min(case_numbers))) / 8
    if float_answer % 1 >= 0.5:
        answer = int(float_answer + 1)
    else:
        answer = int(float_answer)
    print(f'#{test_case} {answer}')