def solution(n):
    result = []
    for i in range(n):
        result.append([0] * n)
        for j in range(n):
            result[i][i] = 1
    return result