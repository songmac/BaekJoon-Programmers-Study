def solution(intStrs, k, s, l):
    return [int(int_strs[s:s+l]) for int_strs in intStrs if int(int_strs[s:s+l]) > k]
