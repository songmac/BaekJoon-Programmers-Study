def solution(picture, k):
    result = []
    for i in range(len(picture)):
        line = ""
        for j in range(len(picture[i])):
            seg = "".join(picture[i][j]*k)
            line += seg
        for _ in range(k):
            result.append(line)
    return result