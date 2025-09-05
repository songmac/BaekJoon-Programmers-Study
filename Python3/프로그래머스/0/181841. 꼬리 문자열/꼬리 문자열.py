def solution(str_list, ex):
    result = ""
    for x in str_list:
        if x.find(ex) != -1:
            continue
        result += x
    return result