def solution(arr, idx):
    # arr : [0, 0, 0, 1]
    # idx : 1
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    else: 
        return -1

