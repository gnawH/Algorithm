n = input()
N = int(n)
result = []

for i in range(1, 55):
    tmp = 0
    sum = 0
    tmp = N-i
    if tmp > 0:
        for j in str(tmp):
            sum += int(j)
        if sum == i:
            result.append(tmp)
    
if result:
    print(min(result))
else:
    print(0)