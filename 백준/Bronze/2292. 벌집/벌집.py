n = int(input())
limit = 1

for i in range(n):
    limit += 6*i
    if limit >= n:
        print(i+1)
        break