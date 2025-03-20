def solution(arr, intervals):
    result = []
    for i in range(intervals[0][0], intervals[0][1] + 1):
        result.append(arr[i])
    for i in range(intervals[1][0], intervals[1][1] + 1):
        result.append(arr[i])
    return result