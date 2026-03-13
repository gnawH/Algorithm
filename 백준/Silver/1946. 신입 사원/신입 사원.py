import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(N)]
    count = 0

    # 1차 점수 기준 정렬
    scores.sort()
    standard_score = N+1

    for st, nd in scores:
        if standard_score > nd:
            standard_score = nd
            count += 1
        else:
            continue
    print(count)