import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    N = int(input())
    ranks = [list(map(int, input().split())) for _ in range(N)]
    count = 0

    # 1차 점수 기준 정렬
    ranks.sort()
    r_stack = []

    for apply in ranks:
        if len(r_stack) == 0:
            r_stack.append(apply)
        else:
            if r_stack[-1][1] > apply[1]:
                r_stack.append(apply)
            else:
                continue

    print(len(r_stack))