def solution(numbers, n):
    tmp = 0
    for i in numbers:
        tmp += i
        if tmp > n:
            return tmp