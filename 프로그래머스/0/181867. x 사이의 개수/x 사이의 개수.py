def solution(myString):
    result = []
    for i in myString.split('x'):
        result.append(len(i))
    return result