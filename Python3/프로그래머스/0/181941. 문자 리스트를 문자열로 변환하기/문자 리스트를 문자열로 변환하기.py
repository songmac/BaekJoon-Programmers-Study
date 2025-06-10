"""
기본 풀이
def solution(arr):
    answer = ''
    for i in arr:
        answer += i
    return answer
"""


def solution(arr):
    return ''.join(arr) # '구분자'.join(반복가능객체)
