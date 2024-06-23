"""
초기 풀이
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
"""

def solution(n, control):
    c = { 'w':1, 's':-1, 'd':10, 'a':-10}
    for i in control:
        n += c[i]
    return n