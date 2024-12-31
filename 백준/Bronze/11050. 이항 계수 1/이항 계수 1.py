def fact(n):
    N = 1
    for i in range(1, n+1):
        N*=i
    return N

n, k = map(int, input().split())
print(int(fact(n)/(fact(k)*fact(n-k))))