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