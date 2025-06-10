def solution(my_string):
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    counts = [0] * len(letters)
    for ch in my_string:
        idx = letters.index(ch)
        counts[idx] += 1
    return counts