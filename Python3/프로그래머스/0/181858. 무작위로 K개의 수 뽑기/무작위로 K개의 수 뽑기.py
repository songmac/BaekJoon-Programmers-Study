def solution(arr, k):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
        else:
            pass
    if len(result) >= k:
        return result[:k]
    elif len(result) < k:
        for _ in range(k-len(result)):
            result.append(-1)
        return result