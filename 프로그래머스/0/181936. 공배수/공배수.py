"""
문제 해석 : 나머지 0인 것이 동시에 충족되면 1, 아니면 0
"""

"""
기본형
def solution(number, n, m):
    if (number % n == 0) and (number % m == 0): # 나누기(/), 몫(//), 나머지(%)
        return 1  
    else :
        return 0
"""

def solution(number, n, m):
    return int((number % n == 0) and (number % m == 0)) # if 구문은 Boolean으로 결과 값이 출력 됨. Ture일때 1로 반환할 수 있도록 int형으로 변환
