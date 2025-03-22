def solution(arr, queries):
    result = []
    for a, b, c in queries:
        tmp = []
        for i in range(a, b+1):
            if arr[i] > c: 
                tmp.append(arr[i])
        if len(tmp) == 0:
            result.append(-1)
        else:
            result.append(min(tmp))
    return result
        