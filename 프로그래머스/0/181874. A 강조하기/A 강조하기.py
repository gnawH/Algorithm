def solution(myString):
    result = ''
    for i in myString.lower():
        if i == 'a':
            result += 'A'
        else:
            result += i
    return result
        