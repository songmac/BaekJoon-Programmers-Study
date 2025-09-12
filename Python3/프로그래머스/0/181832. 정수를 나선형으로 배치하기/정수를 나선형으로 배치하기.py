def solution(n):
    ans = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1

    while num <= n * n:
        for c in range(left, right + 1):
            ans[top][c] = num
            num += 1
        top += 1

        for r in range(top, bottom + 1):
            ans[r][right] = num
            num += 1
        right -= 1

        if top <= bottom:
            for c in range(right, left - 1, -1):
                ans[bottom][c] = num
                num += 1
            bottom -= 1

        if left <= right:
            for r in range(bottom, top - 1, -1):
                ans[r][left] = num
                num += 1
            left += 1

    return ans
