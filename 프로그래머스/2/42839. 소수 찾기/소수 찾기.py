from itertools import permutations

def solution(numbers):
    # 1. 문자열을 한자리 숫자로 분할
    number = [num for num in numbers]
    
    # 2. 조합할 수 있는 모든 경우의 수 찾기
    numbers_permutaions = []
    
    for i in range(1, len(number)+1):
        numbers_permutaions += list(permutations(number, i))
        
    permutations_set = set(int(''.join(num)) for num in numbers_permutaions)
    
    # 3. 소수 판별
    count = 0
    for num in permutations_set:
        isPrime = False
        if num >= 2:
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    isPrime = True
                    break
            if isPrime == False:
                count += 1
    return count