from collections import Counter

def solution(a, b, c, d):
    numbers = [a, b, c, d]
    count = Counter(numbers)
    values = list(count.values())
    keys = list(count.keys()) # 딕셔너리의 key의 개수가 곧, 딕셔너리의 길이
    
    if len(count) == 1:
        # 네 숫자가 모두 같은 경우
        return 1111 * a
    
    elif len(count) == 2:
        if 3 in values:
            # 세 숫자가 같고 나머지 하나가 다른 경우
            p = keys[values.index(3)]
            q = keys[values.index(1)]
            return (10 * p + q) ** 2
        else:
            # 두 숫자가 각각 두 번 나오는 경우
            p, q = keys
            return (p + q) * abs(p - q)
    
    elif len(count) == 3:
        # 세 숫자가 같고 하나만 다른 경우
        p = keys[values.index(2)]
        q = keys[values.index(1)]
        r = keys[values.index(1, values.index(1) + 1)]
        return q * r
    
    else:
        # 네 숫자가 모두 다른 경우
        return min(numbers)