def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        result = []  # 각 쿼리마다 초기화
        for i in range(s, e + 1):        
            if arr[i] > k:
                result.append(arr[i])
                
        if result:
            answer.append(min(result))
        else: 
            answer.append(-1)
                
    return answer
