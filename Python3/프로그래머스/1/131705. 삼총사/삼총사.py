"""
def solution(number):
    cnt = 0
    n = len(number)
    
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if number[i] + number[j] + number[k] == 0:
                    cnt += 1
                    
    return cnt
    
"""


from itertools import combinations

def solution(number):
    cnt = 0
    for comb in combinations(number, 3):
        if sum(comb) == 0:
            cnt += 1
            
    return cnt