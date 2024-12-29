a, b = map(int, input().split())
A = []
B = []
result = []

for i in range(1, a+1):
    if a % i == 0:
        A.append(i)
for j in range(1, b+1):
    if b % j == 0:
        B.append(j)
for k in A:
    if k in B:
        result.append(k)
print(max(result))
print(int(a*b/max(result)))