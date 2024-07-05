def solution(l, r):
    result = []
    for num in range(l, r + 1):
        # 숫자를 문자열로 변환하고 집합으로 만들어 '0'과 '5'로만 이루어졌는지 확인
        digits = set(str(num))
        if digits.issubset({'0', '5'}): 
            result.append(num)
    
    if not result:
        return [-1]
    return result


