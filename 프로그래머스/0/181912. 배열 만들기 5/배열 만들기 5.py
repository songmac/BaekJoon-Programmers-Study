def solution(intStrs, k, s, l):
    answer = []
    for int_strs in intStrs:
        if int(int_strs[s:s+l]) > k:
            answer.append(int(int_strs[s:s+l]))
    return answer
    