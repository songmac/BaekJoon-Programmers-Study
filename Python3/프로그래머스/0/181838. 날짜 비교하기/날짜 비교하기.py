def solution(date1, date2):
    for i in range(len(date1)):
        if date2[i] - date1[i] > 0: return 1
        elif date2[i] -  date1[i] == 0: continue
        else: return 0
    return 0