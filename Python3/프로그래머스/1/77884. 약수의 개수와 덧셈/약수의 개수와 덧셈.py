def solution(left, right):
    result = []
    for i in range(left, right+1):        
        div_lst = [j for j in range(1, i+1) if i % j == 0]
        if len(div_lst) % 2 == 0 :
            result.append(i)
        else :
            result.append(-1 * i)    
    return sum(result)
