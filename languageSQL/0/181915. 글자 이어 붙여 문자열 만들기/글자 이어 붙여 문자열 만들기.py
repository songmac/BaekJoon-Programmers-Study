from collections import defaultdict

def solution(my_string, index_list):
    result = defaultdict()
    for idx, char in enumerate(my_string): 
        result[idx] = char
        
    answer = ''
    for i in index_list:
        answer += result[i]
    
    return answer
