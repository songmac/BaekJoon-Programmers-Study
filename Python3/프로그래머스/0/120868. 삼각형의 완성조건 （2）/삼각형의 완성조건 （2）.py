def solution(sides):
    # 가장 긴 변의 길이가 sides 배열 중 있을 경우 (b가 제일 큰 경우, b < a + c)
    a, b = min(sides), max(sides)
    result1 = [c for c in range(b-a+1, b+1)]
    # 가장 긴 변의 길이가 sides 배열 중 없을 경우 (c가 제일 큰 경우, c < a + b)
    result2 = [c for c in range(b+1, a+b)]

    return len(result1) + len(result2)