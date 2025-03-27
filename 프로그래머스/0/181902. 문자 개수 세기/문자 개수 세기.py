def solution(my_string):
    dict = {}
    for i in range(65, 91):
        dict[i] = 0
    for i in range(97, 123):
        dict[i] = 0
    
    for j in my_string:
        if ord(j) in dict:
            dict[ord(j)] += 1
    
    return([k for k in dict.values()])