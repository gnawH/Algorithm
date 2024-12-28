L = int(input())
eng = list(input())
dict = {}
result = 0
tmp = 0

for i in range(1, 27):
    dict[chr(i+96)] = i

for j in eng:
    result = result + dict[j] * 31**tmp
    tmp+=1

print(result)