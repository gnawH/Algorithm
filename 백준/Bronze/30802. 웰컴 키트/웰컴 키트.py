cnt = 0
n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

for i in size:
    if i%t == 0:
        cnt += int(i/t)
    else:
        cnt += int(i/t+1)
print(cnt)
print(int(n/p), n%p)