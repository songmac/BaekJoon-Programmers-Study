def solution(arr, queries):

    for i, j in queries: # 파이썬의 언패킹(unpacking) 기능을 이용
        arr[i], arr[j] = arr[j], arr[i]
        
    return arr