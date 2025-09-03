def solution(n_str):
    i = 0
    while n_str:
        if n_str[i] == "0":
            n_str = n_str[i+1:]
        else :
            break
    return n_str