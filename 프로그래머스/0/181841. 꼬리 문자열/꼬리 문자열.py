def solution(str_list, ex):
    result = ''
    for i in str_list:
        if ex not in i:
            result += i
    return result