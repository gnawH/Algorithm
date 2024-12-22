t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    if n%h == 0:
            print(str(h)+str(format(int(n/h), '02')))
    else:
        print(str(n%h)+str(format(int(n/h)+1, "02")))