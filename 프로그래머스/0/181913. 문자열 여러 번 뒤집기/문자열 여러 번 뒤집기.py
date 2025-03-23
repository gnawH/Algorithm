def solution(my_string, queries):
    list_my_string = list(my_string)
    
    for a, b in queries:
        stack = []
        for i in range(a, b+1):
            stack.append(list_my_string[i])
            
        for i in range(a, b+1):
            list_my_string[i] = stack.pop()
        
    return (''.join(list_my_string))