def solution(n, k):
    tmp = k
    result = []
    while tmp <= n:
        result.append(tmp)
        tmp += k
    return result