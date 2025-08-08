def solution(binomial):
    a = int(binomial.split()[0])
    b = int(binomial.split()[2])
    op = binomial.split()[1]
    return (a + b) if op == '+' else a - b if op == '-' else (a * b)

# def solution(binomial):
#     return eval(binomial)