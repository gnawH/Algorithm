def solution(num_list):
    m = 1
    for i in num_list:
        m *= i
    if m < sum(num_list)**2:
        return 1
    else:
        return 0
    