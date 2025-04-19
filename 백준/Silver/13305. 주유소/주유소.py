import sys
input = sys.stdin.readline

n = int(input())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))

total = 0
min_price = price[0]

for i in range(n-1):
    if min_price > price[i]:
        min_price = price[i]
        
    total += (min_price * dis[i])
print(total)