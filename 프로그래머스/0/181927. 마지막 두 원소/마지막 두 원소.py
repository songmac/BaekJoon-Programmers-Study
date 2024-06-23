def solution(num_list):
    answer = []
    n = num_list
    i = int(len(n) - 1)

    if n[i] > n[i-1]:
        answer = [n[i] - n[i-1]]
    elif n[i] <= n[i-1]:
        answer = [n[i]*2]
    
    return n + answer