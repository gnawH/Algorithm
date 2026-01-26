from itertools import combinations

N, M = map(int, input().split())
num = [i for i in range(1, N+1)]

comb = list(combinations(num, M))

for com in comb:
    for i in com:
        print(i, end=' ')
    print()