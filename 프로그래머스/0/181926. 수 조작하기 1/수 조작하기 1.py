def solution(n, control):
    for i in control:
        if i == "w":
            n = n + 1
        elif i == "s":
            n = n - 1
        elif i == "d":
            n = n + 10
        elif i == "a":
            n = n - 10
        else :
            continue
    
    return n