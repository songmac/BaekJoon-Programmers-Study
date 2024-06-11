def solution(a, b, c):
    result = 0
    
    if (a != b) and (b != c) and (a != c) :
        result = a + b + c
    elif (a == b) or (b == c) or (a == c) :
        result = (a + b + c) * (pow(a, 2) + pow(b, 2) + pow(c, 2))
        if (a == b) and (b == c) and (a == c):
            result = (a + b + c) * (pow(a, 2) + pow(b, 2) + pow(c, 2)) * (pow(a, 3) + pow(b, 3) + pow(c, 3))
        else :
            pass
    return result