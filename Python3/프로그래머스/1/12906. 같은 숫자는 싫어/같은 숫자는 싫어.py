def solution(arr):
    result = []
    
    for idx, val in enumerate(arr):
        if idx == 0:
            result.append(val)
        else:
            if val == result[-1]:
                pass
            else:
                result.append(val)

    return result