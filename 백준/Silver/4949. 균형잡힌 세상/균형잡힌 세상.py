import sys
input = sys.stdin.readline

while True:
    stc = input().rstrip()
    stack = []
    check = 0
    # 종료 조건
    if stc == '.':
        break
    for i in stc:
        if i == '(':
            stack.append(i)
        elif i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                stack.append(i)
                check = 1
                break
            elif stack[-1] == '(':
                stack.pop()
            else:
                check = 1
                break
        elif i == ']':
            if len(stack) == 0:
                stack.append(i)
                check = 1
                break
            elif stack[-1] == '[':
                stack.pop()
            else:
                check = 1
                break
    if check == 0 and len(stack) == 0:
        print('yes')
    else:
        print('no')
