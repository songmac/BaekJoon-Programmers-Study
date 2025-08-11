# def solution(arr):
#     X = []
#     for a in arr:
#         for i in range(a):
#             X.append(a)
#     return X


def solution(arr):
    return [a for a in arr for i in range(a)]