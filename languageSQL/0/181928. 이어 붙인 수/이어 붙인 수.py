"""
초기 코드
def solution(num_list):
    
    odd_n = ''
    even_n = ''
    
    for n in num_list:
        if (n % 2) == 1 : 
            odd_n += str(n)
        else : 
            even_n += str(n)
            
    return int(odd_n) + int(even_n)
"""

def solution(num_list):
    return int(''.join([str(x) for x in num_list if x % 2])) + int(''.join([str(x) for x in num_list if not x % 2]))