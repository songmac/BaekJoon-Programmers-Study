import math

"""
# gcd 동작 원리 : 유클리드 호제법
def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
"""

def solution(numer1, denom1, numer2, denom2):
    # 분수를 더함
    result_numer = numer1 * denom2 + numer2 * denom1  # 분자
    result_denom = denom1 * denom2  # 분모
    
    # 결과를 기약 분수로 만듦
    gcd = math.gcd(result_numer, result_denom)  # 최대 공약수를 나타냄 
    result_numer //= gcd
    result_denom //= gcd
    
    return [result_numer, result_denom]