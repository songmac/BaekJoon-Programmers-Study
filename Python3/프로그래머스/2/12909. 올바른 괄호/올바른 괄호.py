def solution(s):
    balance = 0  # 균형을 확인하는 변수
    for char in s:  # 문자열 s의 각 문자를 순회
        if char == '(':  # 여는 괄호인 경우
            balance += 1
        else:  # 닫는 괄호인 경우
            balance -= 1
            if balance < 0:  # balance가 음수이면 닫는 괄호가 더 많음
                return False  # 짝이 맞지 않으므로 False 반환
    return balance == 0  # balance가 0이면 짝이 맞으므로 True, 아니면 False