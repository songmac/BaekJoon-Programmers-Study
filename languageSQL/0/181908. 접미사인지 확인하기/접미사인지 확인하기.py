def solution(my_string, is_suffix):
    result = [my_string[len(my_string)-i:] for i in range(1, len(my_string)+1)]
    return 1 if is_suffix in result else 0