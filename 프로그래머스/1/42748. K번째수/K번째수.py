def solution(array, commands):
    answer = []
    # [1, 5, 2, 6, 3, 7, 4]
    for c in commands:
        tmp = []
        i, j, k = c[0], c[1], c[2]  # 2, 5, 3
        for a in range(i-1, j):
            tmp.append(array[a])
        tmp.sort()
        answer.append(tmp[k-1])
    return answer