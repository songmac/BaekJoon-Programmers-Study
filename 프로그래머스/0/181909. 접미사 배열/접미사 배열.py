def solution(my_string):
    result = []
    for i in range(0, len(my_string)+1):
        result.append(my_string[len(my_string)-i:])
    return sorted(result[1::])