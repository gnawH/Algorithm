t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    naver = [i for i in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            naver[j] += naver[j-1]
    print(naver[-1])
    