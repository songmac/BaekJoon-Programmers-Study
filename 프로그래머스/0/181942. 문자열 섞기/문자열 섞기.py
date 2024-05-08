def solution(str1, str2):
    answer = "" # (문자열 불변성) 선언이유 : 빈 문자열을 초기화하여 이후 문자열을 누적시키기 위함 
    for i in range(len(str1)):
        answer += str1[i] + str2[i]
    return answer

"""
1. 리스트 이용
def solution(str1, str2):
    return ''.join(str1[i] + str2[i] for i in range(len(str1)))
"""
