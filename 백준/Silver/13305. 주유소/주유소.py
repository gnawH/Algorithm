import sys
input = sys.stdin.readline

n = int(input())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))

total = 0

for i in range(n-1):
    if price[i] >= price[i+1]:
        total += (price[i] * dis[i])
    else:
        if dis[-1] == dis[i]:
            break
        total += (price[i] * (dis[i] + dis[i+1])) 
        if price[i+1]:
            price[i+1] = 0
print(total)