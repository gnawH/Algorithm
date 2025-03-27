def solution(my_string, indices):
    result = ''
    for i in range(len(my_string)):
        if i in indices:
            continue
        else:
            result += my_string[i]

    return result
            