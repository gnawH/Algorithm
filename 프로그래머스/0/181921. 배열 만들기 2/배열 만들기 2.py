def solution(l, r):
    result = []
    num = ['1', '2', '3', '4', '6', '7', '8', '9']
    for i in range(l, r+1):
        tmp = False
        for j in range(len(str(i))):
            if str(i)[j] in num:
                tmp = True
            elif j == len(str(i))-1 and tmp == False:
                result.append(i)
    if len(result) == 0:
        return [-1]
    else:
        return result
                
                
            
            