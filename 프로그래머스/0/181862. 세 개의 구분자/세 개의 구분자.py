def solution(myStr):
    newStr = ''
    for i in range(len(myStr)):
        if myStr[i] in ['a', 'b', 'c']:
            newStr += ' '
        else:
            newStr += myStr[i]
    
    if len(list(newStr.split())) == 0:
        return ['EMPTY']
    else:
        return list(newStr.split())