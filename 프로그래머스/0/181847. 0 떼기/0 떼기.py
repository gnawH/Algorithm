def solution(n_str):
    for i, v in enumerate(n_str):
        if v != '0':
            return n_str[i:]
            