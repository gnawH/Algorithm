n = int(input())
pbag = []
for i in range(n+1):
    for j in range(n+1):
        if (5 * i) + (3 * j) == n:
            pbag.append(i+j)
if len(pbag) == 0:
    print(-1)
else:
    print(min(pbag))