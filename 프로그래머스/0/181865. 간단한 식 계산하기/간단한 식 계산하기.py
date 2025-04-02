def solution(binomial):
    cal = binomial.split()
    if cal[1] == '+':
        return int(cal[0]) + int(cal[-1])
    elif cal[1] == '-':
        return int(cal[0]) - int(cal[-1])
    elif cal[1] == '*':
        return int(cal[0]) * int(cal[-1])