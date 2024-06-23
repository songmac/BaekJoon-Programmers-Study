"""
초기 풀이
def solution(num_list):
    answer = []
    n = num_list
    i = int(len(n) - 1)

    if n[i] > n[i-1]:
        answer = [n[i] - n[i-1]]
    elif n[i] <= n[i-1]:
        answer = [n[i]*2]
    
    return n + answer
"""


def solution(num_list):
    n1, n2 = num_list[-1], num_list[-2]
    if n1 > n2:
        num_list.append(n1 - n2)
    else :
        num_list.append(n1 * 2)
    return num_list