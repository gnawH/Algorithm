def solution(arr):
    result = []
    i = 0
    while i < len(arr):
        if len(result) == 0:
            result.append(arr[i])
            i += 1
        elif result[-1] < arr[i]:
            result.append(arr[i])
            i += 1
        else:
            result.pop()
    return result