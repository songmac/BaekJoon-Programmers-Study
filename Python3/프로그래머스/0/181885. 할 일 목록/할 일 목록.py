def solution(todo_list, finished):
    result = []
    for idx, val in enumerate(finished):
        if val == False: # bool 자료형은 비교 연산 시, 대문자 True / False 로 입력해야 함
            result.append(todo_list[idx])
    return result