def solution(a, d, included):
    result = 0
    for i in range(len(included)):
        if i != 0:
            a += d
        if included[i] == True:
            result += a
    return result