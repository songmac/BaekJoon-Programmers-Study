def solution(k, m, score):
    score.sort(reverse=True)

    a = []
    box_sum = 0
    for i in range(len(score) // m): 
        a.append(min(score[m*i:m*(i+1)]) * m)
        box_sum += a[i]

    return box_sum
