def solution(numbers, n):
    total = 0 # sum이라는 예약어를 변수로 사용하면 
              # 그 다음에 sum() 기능을 수행할 때 인식이 안되므로 
              # 해당 부분에 대해 주의가 필요함
    for i in numbers:
        total += i
        if total > n:
            return total

"""
def solution(numbers, n):
    sum_lst = []
    for i in numbers:
        sum_lst.append(i)
        if sum(sum_lst) > n: # 매번 sum() 함수를 호출하면 위 코드에 비해 
                             # 시간 복잡도가 O(1)->O(n)로 증가하며 메모리 성능이 떨어짐
            return sum(sum_lst)
"""
