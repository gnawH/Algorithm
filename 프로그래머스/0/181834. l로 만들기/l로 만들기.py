def solution(myString):
    for i in myString:
        if ord(i) < 108:
            myString = myString.replace(i, 'l')
    return myString