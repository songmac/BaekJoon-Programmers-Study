def solution(my_strings, parts):
    answer = ''
    for my_str, (s, e) in zip(my_strings, parts):
        answer += my_str[s: e+1]
    return answer