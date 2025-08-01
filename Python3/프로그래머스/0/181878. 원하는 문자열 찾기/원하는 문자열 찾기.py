def solution(myString, pat):
    if len(myString) < len(pat):
        return 0
    else :
        if pat.lower() in myString.lower():  
            return 1
        else : 
            return 0