def solution(arr):
    # i = 0, 1, 2, 3, 4, 5, 6, 7, ... -> n = pow(2, i)
    # n = 1, 2, 4, 8, 16, 32, 64, 128, ...

    for i in range(len(arr), 0, -1):
        # 배열 길이가 2의 정수 거듭제곱일 경우
        if len(arr) % pow(2, i) == 0:  # 작은 수로 먼저 나누는 일이 없도록 큰 숫자부터 셈
            result = arr
        elif len(arr) % pow(2, i) == 1:
            result = arr
            
        # 배열 길이가 2의 거듭제곱이 아닐 경우
        else : 
            if pow(2, i-1) < len(arr):
                result = arr
                for _ in range(pow(2, i)-len(arr)):
                    result.append(0)
    return result