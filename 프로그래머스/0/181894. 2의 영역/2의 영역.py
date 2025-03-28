def solution(arr):
    result = []
    for i in range(len(arr)):
        if arr[i] == 2:
            result.append(i)
    if len(result) == 0:
        return [-1]
    elif len(result) == 1:
        return [2]
    else:
        a, b = result[0], result[-1]
        return arr[a:b+1]
        