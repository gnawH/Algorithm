def solution(num_list):
    h, j = '', ''
    for i in num_list:
        if i % 2 == 0:
            j += str(i)
        else:
            h += str(i)
    return int(j) + int(h)
            