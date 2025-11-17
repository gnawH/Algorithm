T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    flies = []
    died_files = []
    for _ in range(N):
        flies.append(list(map(int, input().split())))

    for i in range(N-M+1):
        for j in range(N-M+1):
            tmp = 0
            for idx in range(M):
                tmp += sum(flies[i+idx][j:j+M])
            died_files.append(tmp)
    print(f'#{test_case} {max(died_files)}')