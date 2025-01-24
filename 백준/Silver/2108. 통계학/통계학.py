import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for i in range(N)]
s_arr = sorted(arr)
dict = {}
max_num = 0
new = []

print(round(sum(arr) / N))
print(s_arr[N//2])

for i in s_arr:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
    max_num = max(max_num, dict[i])

for k, v in dict.items():
    if v == max_num:
        new.append(k)

if len(new) > 1:
    print(new[1])
else:
    print(new[0])

print(max(arr)-min(arr))