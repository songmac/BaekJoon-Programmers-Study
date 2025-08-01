def solution(arr):
    count = 0
    while True:
        next_arr = [i / 2 if i >= 50 and i % 2 == 0 else i * 2 + 1 if i < 50 and i % 2 == 1 else i for i in arr]
        if arr == next_arr:
            break
        arr = next_arr
        next_arr = []
        count += 1
    return count