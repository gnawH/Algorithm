L = int(input())
eng = list(input())
result = 0
tmp = 0

for j in eng:
    result += (ord(j)-96) * 31**tmp
    tmp += 1

print(result % 1234567891)