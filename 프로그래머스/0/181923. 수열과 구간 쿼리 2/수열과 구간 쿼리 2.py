def solution(arr, queries):
    result = []
    for a, b, c in queries:
        tmp = []
        for i in arr[a:b+1]:
            if i > c:
                tmp.append(i)
        if len(tmp) == 0:
            result.append(-1)
        else:
            result.append(min(tmp))
    return result
        