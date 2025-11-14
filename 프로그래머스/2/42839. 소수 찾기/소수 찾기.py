from itertools import permutations

def solution(numbers):
    result = 0
    num = [number for number in numbers]
    per = []
    
    for count in range(1, len(num)+1):
        per += list(permutations(num, count))
        
    per_num = set(int(''.join(p)) for p in per)
    result += prime_number(per_num)
    return result
    
    
def prime_number(per_num):
    result = 0
    for num in per_num:
        count = 0
        if num >= 2:
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    count += 1
                    break
            if count == 0:
                result += 1
                
    return result
            