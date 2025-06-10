"""
기본형
def solution(a, b, flag):
    if flag == True :
        result = a + b
    elif flag == False :
        result = a - b
    else :
        pass
        
    return result
"""

def solution(a, b, flag):
    if flag == False :
        b *= -1
    else :
        pass
        
    return a + b
