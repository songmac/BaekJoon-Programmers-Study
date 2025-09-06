import math

def solution(a, b):
    if a % 2 == 1 and b % 2 == 1:
        return math.pow(a,2) + math.pow(b,2)
    elif a % 2 == 1 or b % 2 == 1:
        return 2 * (a + b)
    else:
        return abs(a - b) # 절대값은 내장 함수 이용