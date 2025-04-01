def solution(myString, pat):
    result = ''
    for i in range(len(myString)):
        if myString[i] == pat[0]:
            if myString[i:i+len(pat)] == pat:
                result = myString[:i+len(pat)]
    return result
                  