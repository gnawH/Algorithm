N, M = map(int, input().split())

bucket = [0] * (N+1)

for _ in range(M):
    i, j, k = map(int, input().split())
    for l in range(i, j+1):
        bucket[l] = k

for i in bucket[1:]:
    print(i, end=' ')