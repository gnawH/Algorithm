import sys
input = sys.stdin.readline
n = int(input())
stack = []

for i in range(n):
    a = input()
    if 'push' in a:
        a, b = a.split()
        stack.append(int(b))
    elif 'pop' in a:
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif 'size' in a:
        print(len(stack))
    elif 'empty' in a:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif 'top' in a:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])