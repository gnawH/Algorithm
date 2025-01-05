n = int(input())
sum = 1
cnt = 0

for i in range(1, n+1):
    sum *= i
    
for i in str(sum)[::-1]:
    if i == '0':
        cnt += 1
    else:
        print(cnt)
        break
