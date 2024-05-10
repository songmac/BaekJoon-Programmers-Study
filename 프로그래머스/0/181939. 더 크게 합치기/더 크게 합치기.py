def solution(a, b):
    A, B = str(a), str(b)
    int1, int2 = int(A+B), int(B+A) 
    
    if int1 >= int2 : # int자료형은 join함수를 쓸 수 없음
        answer = int1
    elif int1 < int2 :
        answer = int2
                   
    return answer