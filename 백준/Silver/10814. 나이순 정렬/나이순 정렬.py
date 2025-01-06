n = int(input())
list = []

for i in range(n):
    age, name = input().split()
    list.append([int(age), name, i])

list.sort(key=lambda x : (x[0], x[2]))
for i in range(n):
    print(list[i][0], list[i][1])