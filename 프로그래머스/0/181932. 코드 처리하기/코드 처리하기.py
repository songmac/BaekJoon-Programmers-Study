def solution(code):
    mode = 0  # mode를 함수 내부에서 0으로 초기화
    ret = ""  # 결과를 저장할 문자열 초기화

    # 문자열 code의 각 문자에 대해 반복, 인덱스와 함께 반복
    for idx in range(len(code)):
        char = code[idx]
        if mode == 0:
            if char != '1':
                if idx % 2 == 0:
                    ret += char
            else:
                mode = 1
        elif mode == 1:
            if char != '1':
                if idx % 2 != 0:
                    ret += char
            else:
                mode = 0

    # ret 문자열이 비어있으면 "EMPTY" 반환, 그렇지 않으면 ret 반환
    return ret if ret else "EMPTY"