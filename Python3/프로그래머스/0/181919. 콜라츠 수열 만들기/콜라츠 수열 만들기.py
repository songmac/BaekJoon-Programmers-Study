def solution(n):
    answer = []
    answer.append(n)
    
    while n > 1:    
        if n % 2 == 0 :
            n = int(n / 2)
            answer.append(n)
        elif n % 2 == 1 :
            n = int((3 * n) + 1)
            answer.append(n)

    return answer
