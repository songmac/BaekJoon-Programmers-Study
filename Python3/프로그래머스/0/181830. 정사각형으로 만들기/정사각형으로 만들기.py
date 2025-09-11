def solution(arr):
    n_max = len(arr) if len(arr) > len(arr[0]) else (len(arr[0]))
    n_max = max(len(arr), len(arr[0]))
    n_arr = [[0 for _ in range(n_max)] for _ in range(n_max)]
    
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            n_arr[i][j] = arr[i][j]
    
    return n_arr