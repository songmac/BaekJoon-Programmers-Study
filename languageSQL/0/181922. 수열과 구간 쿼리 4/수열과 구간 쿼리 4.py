"""
문제 해설 : i가 k의 배수이면 (여기서, i는 배열의 인덱스 자리를 말함)
"""

def solution(arr, queries):
    answer = []
    for _ in range(len(queries)):
        for s, e, k in queries:

            for i, v in enumerate(arr):
                if (s <= i <= e) & (i % k == 0) :
                    arr[i] += 1
                    
        answer = arr

        return answer
