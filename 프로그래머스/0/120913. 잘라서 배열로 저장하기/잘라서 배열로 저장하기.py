def solution(my_str, n):
    answer = []
    for i in range(n, len(my_str)+n, n):
        answer.append(my_str[i-n:i])
    return answer