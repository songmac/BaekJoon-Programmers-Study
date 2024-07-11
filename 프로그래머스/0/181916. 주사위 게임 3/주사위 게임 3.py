from collections import Counter
"""
collections : 고성능의 컨테이너 데이터형을 제공하는 모듈
Counter : 리스트나 다른 반복 가능한(iterable) 객체에서 요소의 빈도를 셀 때 유용하게 사용
"""

def solution(a, b, c, d):
    numbers = [a, b, c, d]
    count = Counter(numbers) # 딕셔너리로 저장
    values = list(count.values()) # 값이 나온 횟수
    keys = list(count.keys()) # 주사위 굴렸을 때 나온 숫자
                              # 딕셔너리의 key의 개수가 곧, 딕셔너리의 길이
    
    if len(count) == 1: 
        return 1111 * a
    elif len(count) == 2:
        if 3 in values:
            p = keys[values.index(3)] 
            q = keys[values.index(1)]
            return (10 * p + q) ** 2
        elif 2 in values:
            p, q = keys
            return (p + q) * abs(p - q)
        
    elif len(count) == 3:
        p = keys[values.index(2)]
        remaining_keys = [k for k, v in count.items() if v == 1]
        q, r = remaining_keys
        return q * r
    
    else:   
        return min(numbers)
    
# index 메서드는 리스트에서 특정 값이 처음으로 나타나는 위치(인덱스)를 반환
"""
이해를 위한 예시
    numbers = [1, 2, 3, 2, 1]
        print(numbers.index(2))  # 결과는 1, 숫자 2가 처음 나타나는 위치
        print(numbers.index(2, 2))  # 결과는 3, 인덱스 2 이후에 숫자 2가 처음 나타나는 위치
"""
