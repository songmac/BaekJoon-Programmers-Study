def solution(s):
    s_lst = s.split(" ")

    new_lst = []
    for s_str in s_lst:
        if s_str == "Z":
            if len(new_lst) != 0: 
                new_lst.pop()
            else:
                continue
        else:
            new_lst.append(int(s_str))
    
    return sum(new_lst)