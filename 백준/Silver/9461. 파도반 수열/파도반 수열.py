T = int(input())

P = [0] * 101
P[1:11] = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(11, 101):
    P[i] = P[i - 5] + P[i - 1]

for test_case in range(T):
    N = int(input())
    print(P[N])