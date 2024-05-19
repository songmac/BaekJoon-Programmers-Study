"""
def solution(a, d, included):
    n = len(included)
    sum = 0
    
    for i in range(n): 
        if included[i]: # if included[i] == True: / if bool(included[i]): / if included[i] is True:
            sum += a + d * i
            
    return sum
"""

    
def solution(a, d, included):
    sum_list = []
    total_sum = 0
    
    for i in range(len(included)): 
        sum_list.append(a + d * i)
        if included[i]: 
            total_sum += sum_list[-1]
            
    return total_sum
