def solution(picture, k):
    result = []
    for i in picture:
        tmp = ''
        for j in i:
            tmp += (j*k)
        for kk in range(k):
            result.append(tmp)
            
    return result