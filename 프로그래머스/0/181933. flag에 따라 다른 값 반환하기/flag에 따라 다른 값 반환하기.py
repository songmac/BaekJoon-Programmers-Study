def solution(a, b, flag):
    if flag == True :
        operator = '+'
        result = a + b
    elif flag == False :
        operator = '-'
        result = a - b
    else :
        pass
        
    return result
