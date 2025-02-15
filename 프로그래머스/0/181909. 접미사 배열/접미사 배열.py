def solution(my_string):
    result = [my_string[len(my_string)-i:] for i in range(1, len(my_string)+1)]
    return sorted(result)