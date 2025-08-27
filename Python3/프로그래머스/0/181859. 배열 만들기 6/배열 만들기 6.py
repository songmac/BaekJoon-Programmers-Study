def solution(arr):
    stk = []
    for i in range(len(arr)):
        if len(stk) == 0:
            stk.append(arr[i])
        else :
            if stk[-1] == arr[i]:
                stk.pop()
            elif stk[-1] != arr[i]:
                stk.append(arr[i])
    if len(stk) == 0:
        return [-1]    
    return stk