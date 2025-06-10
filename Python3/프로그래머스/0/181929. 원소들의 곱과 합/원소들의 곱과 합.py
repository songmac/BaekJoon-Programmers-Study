"""
초기 코드
def solution(num_list):    
    multi_num = 1
    sum_num = 0
    sum_pow = 0
    
    for i in num_list:
        multi_num *= i
        sum_num += i
        
    sum_pow = pow(sum_num, 2)
        
    if multi_num < sum_pow :
        return 1
    elif multi_num > sum_pow :
        return 0
"""
    
    
def solution(num_list):
    mul = 1 
    for n in num_list:
        mul *= n
    return int(mul < sum(num_list) ** 2)