"""
초기 풀이
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
"""

def solution(arr, queries):
    results = []
    
    for s, e, k in queries: 
        result = [arr[i] for i in range(s, e+1) if arr[i] > k]

        if result:
            results.append(min(result))
        else: 
            results.append(-1)

    return results