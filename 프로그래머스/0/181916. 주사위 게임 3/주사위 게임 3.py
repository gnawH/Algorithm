def solution(a, b, c, d):
    
    tmp = 1
    score = 0
    dic = {}
    dice = [a, b, c, d]
    
    for i in dice:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    sorted_dict = dict(sorted(dic.items(), key = lambda x:x[1]))
    print(sorted_dict)
            
    for k, v in sorted_dict.items():
        if v == 4:
            score = (1111 * a)
        elif v == 1 and len(sorted_dict) == 2:
            score = k
        elif v == 3:
            score += (10 * k)
            score = score **2
        elif v == 2 and len(sorted_dict) == 2:
            if score == 0:
                score = k
            else:
                score = (score + k) * abs(score - k)
            
        elif v == 1 and len(sorted_dict) == 3:
            tmp *= k
            score = tmp
        elif v == 1 and len(sorted_dict) == 4:
            score = min(sorted_dict.keys())
            break
    return score
    