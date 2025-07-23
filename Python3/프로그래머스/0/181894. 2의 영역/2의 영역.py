def solution(arr):
    answer = [idx for idx, val in enumerate(arr) if val // 2 == 1 and val % 2 == 0]
    return [-1] if len(answer) == 0 else arr[answer[0]:answer[-1]+1] 
