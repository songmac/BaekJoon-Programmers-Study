def solution(arr, queries):
    for i, j in queries:
        arr[i: j+1] = [x+1 for x in arr[i: j+1]]
    return arr
