def solution(ineq, eq, n, m):
    if ineq+eq == '>=':
        if n >= m:
            return 1
        else:
            return 0
    elif ineq+eq == '<=':
        if n <= m:
            return 1
        else:
            return 0
    elif ineq+eq == '>!':
        if n > m:
            return 1
        else:
            return 0
    elif ineq+eq == '<!':
        if n < m:
            return 1
        else:
            return 0
        