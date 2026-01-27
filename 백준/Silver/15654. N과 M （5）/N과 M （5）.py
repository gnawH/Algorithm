from itertools import permutations

N, M = map(int, input().split())

per_list = list(permutations(list(map(int, input().split())), M))
for pair in sorted(per_list):
    for num in pair:
        print(num, end=' ')
    print()