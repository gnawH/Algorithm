import sys
input = sys.stdin.readline

n = int(input())
times = []
count = 0
prv_end = 0
for i in range(n):
    start, end = map(int, input().split())
    times.append([start, end])

end_sorted_num = sorted(times, key = lambda x : (x[1], x[0]))

for start, end in end_sorted_num:
    if prv_end <= start:
        count += 1
        prv_end = end

print(count)