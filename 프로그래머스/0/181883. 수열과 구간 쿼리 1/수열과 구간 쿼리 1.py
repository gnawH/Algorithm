def solution(arr, queries):
    for h in queries:
        s, e = h
        for i in range(s, e+1):
            arr[i] += 1
    return arr
        
        