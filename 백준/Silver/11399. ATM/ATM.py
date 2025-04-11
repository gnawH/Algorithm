n = int(input())
time = sorted(list(map(int, input().split())))
sum = 0

for i in range(n):
    sum += (time[i] * (n-i))

print(sum)