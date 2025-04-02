def solution(myString):
    result = myString.split('x')
    for i in result[:]:
        if i == '':
            result.remove(i)
    return sorted(result)