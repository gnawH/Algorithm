n = int(input())
tmp = 0

while n >= 0:
    if n % 5 == 0:
        tmp += (n//5)
        print(tmp)
        break
    n -= 3
    tmp += 1
    
else:
    print(-1)
    