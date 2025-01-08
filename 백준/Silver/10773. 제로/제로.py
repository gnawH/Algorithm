import sys
input = sys.stdin.readline
k = int(input())
list = []

for i in range(k):
    num = int(input())
    if num != 0:
        list.append(num)
    else:
        list.pop()
        
print(sum(list))