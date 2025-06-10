def solution(ineq, eq, n, m):
    if eq == '!':
        operator = ineq 
    else:
        operator = ineq + eq  

    if operator == '<':
        return int(n < m)
    elif operator == '>':
        return int(n > m)
    elif operator == '<=':
        return int(n <= m)
    elif operator == '>=':
        return int(n >= m)
    else:
        return 0
