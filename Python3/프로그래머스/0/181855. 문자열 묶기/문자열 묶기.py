from collections import defaultdict

def solution(strArr):
    arr_dict = defaultdict(int)
    for arr in strArr:
        arr_dict[len(arr)] += 1
    return max(arr_dict.values())