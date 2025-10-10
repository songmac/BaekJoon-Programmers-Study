from collections import deque

def solution(priorities, location):

    queue = deque([(i, p) for i, p in enumerate(priorities)])
    cnt = 0
    
    while queue:
        cur_que = queue.popleft() # (, ) 형태의 튜플
        if any(cur_que[1] < que[1] for que in queue): # 우선순위 크기 비교 : 처음 뽑은 것 vs 그 다음 순서인 것
            queue.append(cur_que) # 크기가 작으면 빼서 맨 뒤로 붙이기
        else: 
            cnt += 1 # popleft 하지 않은(순서 fix) 갯수
            if cur_que[0] == location: # 현재 popleft한 queue에서 인덱스 번호 검사 
                return cnt # fix된 순서 출력
            