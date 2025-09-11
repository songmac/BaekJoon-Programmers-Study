def solution(n):
    answer = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            answer[i][j] = 0
            if i == j:
                answer[i][j] = 1
    return answer