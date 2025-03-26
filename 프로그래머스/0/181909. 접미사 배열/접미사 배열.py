def solution(my_string):
    result = [my_string[i:] for i in range(len(my_string))]
    result.sort()
    return result