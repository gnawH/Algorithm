import sys
input = sys.stdin.readline

while True:
    stc = input().rstrip()
    if stc == '.':
        break  # 종료 조건

    stack = []
    is_balanced = True  # 괄호 균형 여부를 추적하는 플래그

    for i in stc:
        if i in "([":  
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] != '(':
                is_balanced = False
                break
            stack.pop()
        elif i == ']':
            if not stack or stack[-1] != '[':
                is_balanced = False
                break
            stack.pop()

    # 결과 출력
    if is_balanced and not stack:
        print('yes')
    else:
        print('no')
