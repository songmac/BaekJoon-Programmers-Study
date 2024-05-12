def solution(n):
    answer = 0
    if n % 2 == 1 :
        for i in range(1, n+1):
            if i % 2 == 1 :
                answer += i
            else :
                answer += 0
    elif n % 2 == 0 :
        for i in range(1, n+1):
            if i % 2 == 0 :
                answer += pow(i, 2)
            else :
                answer += 0
    return answer