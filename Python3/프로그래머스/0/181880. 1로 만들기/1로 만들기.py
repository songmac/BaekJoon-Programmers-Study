def solution(num_list):
    cnt = 0
    while True:
        for idx, val in enumerate(num_list):
            if (val % 2 == 0):
                num_list[idx] = int(val / 2)
            elif val % 2 == 1:
                if val != 1:
                    num_list[idx] = int((val - 1) / 2)
                else : 
                    continue
            cnt += 1
        if sum(num_list) == len(num_list):
            break
    return cnt