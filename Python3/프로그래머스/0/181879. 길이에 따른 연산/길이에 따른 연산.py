def solution(num_list):
    if len(num_list) <= 10:
        answer = 1
        for i in num_list:
            answer *= i
    else :
        answer = 0
        for i in num_list:
            answer += i
    return answer