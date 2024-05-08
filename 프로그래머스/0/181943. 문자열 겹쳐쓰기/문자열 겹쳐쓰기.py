def solution(my_string, overwrite_string, s):
    a = len(my_string[:s])
    b = len(overwrite_string)
    answer = my_string[:s] + overwrite_string[:b] + my_string[a+b:]
    return answer

"""
좀 더 간결한 표현
answer = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
"""


"""
다른 풀이
def solution(my_str, over_str, s):
    a = my_str
    b = over_str
    answer = a[:s] + b[:len(b)] + a[len(a[:s])+len(b):]
    return answer    
"""


            