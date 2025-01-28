import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
    exit()
    
score = [int(input()) for i in range(n)]
total = 0

if int(n * 0.15 + 0.5) == int(n * 0.15):
    cnt = int(n * 0.15)
elif int(n * 0.15 + 0.5) != int(n * 0.15):
    cnt = int(n * 0.15 + 0.5)

score.sort()
total = score[cnt:n-cnt]
if len(total) == 0:
    print(0)
else:
    if int(sum(total)/len(total) + 0.5) == int((sum(total)/len(total))):
        print(int(sum(total)/len(total)))
    elif int(sum(total)/len(total) + 0.5) != int((sum(total)/len(total))):
        print(int(sum(total)/len(total) + + 0.5))