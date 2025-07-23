def solution(arr, intervals):
    answer = []
    for i in intervals:
        n1, n2 = i
        answer.extend(arr[n1 : n2+1])
    return answer