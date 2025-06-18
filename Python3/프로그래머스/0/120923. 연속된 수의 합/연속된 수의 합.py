def solution(num, total):
    # total을 num으로 나눈 몫을 중심으로 한 범위로 설정
    start = total // num - num // 2
    end = total // num + num // 2 + 1
    
    for i in range(start, end):
        # 현재의 i를 시작으로 num개의 연속된 수를 더함
        answer = [i + j for j in range(num)]
        
        # 연속된 수의 합이 total과 같으면 결과를 반환
        if sum(answer) == total:
            return answer
