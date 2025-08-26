def solution(arr, flag):
    result = []
    for i in range(len(arr)):
        if int(flag[i]): 
            for _ in range(arr[i]):
                result.extend([arr[i], arr[i]])
        else:
            for _ in range(arr[i]):
                result.pop()
    return result