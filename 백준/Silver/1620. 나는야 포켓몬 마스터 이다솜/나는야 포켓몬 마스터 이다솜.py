import sys
N, M = map(int, sys.stdin.readline().strip().split())

pocketmon_number_dict = {pocketmon_number:input() for pocketmon_number in range(1, N+1)}
pocketmon_dict = {pocketmon_number_dict[pocketmon_number]:pocketmon_number for pocketmon_number in range(1, N+1)}

for _ in range(M):
    problem = sys.stdin.readline().strip()
    if ord(problem[0]) >= 47 and ord(problem[0]) <= 57: # 0~9 ASCII CODE
        print(pocketmon_number_dict[int(problem)])
    else:
        print(pocketmon_dict[problem])