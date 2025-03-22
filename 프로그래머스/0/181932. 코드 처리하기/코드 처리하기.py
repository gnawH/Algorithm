def solution(code):
    mode = False
    result = ''
    for i in range(len(code)):
        if code[i] == '1' and mode == False:
            mode = True
        elif code[i] != '1' and mode == False:
            if i % 2 == 0:
                result += code[i]
        elif code[i] == '1' and mode == True:
            mode = False
        elif code[i] != '1' and mode == True:
            if i % 2 == 1:
                result += code[i]
    if result == '':
        return "EMPTY"
    else:
        return result
            
            
            