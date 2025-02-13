def solution(my_strings, parts):
    return ''.join([my_str[s:e+1] for my_str, (s, e) in zip(my_strings, parts)])