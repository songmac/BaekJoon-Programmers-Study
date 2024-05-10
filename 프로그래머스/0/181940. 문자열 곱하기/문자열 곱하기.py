"""
기본풀이
def solution(my_string, k):
    answer = ''
    for i in range(k):
        answer += my_string
    return answer
"""

def solution(my_string, k):
    return my_string*k


"""
def solution(my_string, k):
    return ''.join(my_string)*k
"""