def solution(participant, completion):
    
    dict = {}
    
    for i in participant:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
        
    for j in completion:
        dict[j] -= 1
    
    for k, v in dict.items():
        if v >= 1:
            return k
    
    
    
    