a, b, v = map(int, input().split())

if (v-a)%(a-b) == 0:
    print(int(((v-b)/(a-b))))
else:
    print(int(((v-b)/(a-b)))+1)