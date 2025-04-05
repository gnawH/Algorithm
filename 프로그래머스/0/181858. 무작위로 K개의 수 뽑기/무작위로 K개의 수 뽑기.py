def solution(arr, k):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
    
    while len(result) < k:
        result.append(-1)
        
    return result[:k]