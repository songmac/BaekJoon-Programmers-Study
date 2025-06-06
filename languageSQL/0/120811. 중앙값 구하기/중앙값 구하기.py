def solution(array):
    array.sort()
    mid_index = round(len(array) // 2, 2)
    answer = array[mid_index]
    return answer