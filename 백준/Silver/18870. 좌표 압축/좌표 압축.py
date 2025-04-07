# import sys
# input = sys.stdin.readline

# n = int(input())
# X = tuple(map(int, input().split()))
# sorted_X = sorted(set(X))
# for i in X:
#     for j in range(len(sorted_X)):
#         if i == sorted_X[j]:
#             print(j, end=' ')
#             break

import sys
input = sys.stdin.readline

n = int(input())
X = list(map(int, input().split()))

SX = sorted(set(X))
dict = {v : i for i, v in enumerate(SX)}

for i in X:
    print(dict[i], end=' ')