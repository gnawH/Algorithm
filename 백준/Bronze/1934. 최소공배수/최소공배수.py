import sys
input = sys.stdin.readline

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    r = gcd(a, b)
    print(a*b // r)
    