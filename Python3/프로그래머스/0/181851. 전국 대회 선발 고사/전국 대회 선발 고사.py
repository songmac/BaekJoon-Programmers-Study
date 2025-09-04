def solution(rank, attendance):
    zip_val = []
    zip_idx = []
    result = {}
    
    for idx, val in enumerate(rank): # idx: 참가번호, val: 등수
        if attendance[idx]:
            zip_val.append(val)
            zip_idx.append(idx)

    result = dict(zip(zip_val, zip_idx))
    print(result) # {7: 1, 2: 2, 5: 3, 4: 4}
    print(result.items()) # dict_items([(7, 1), (2, 2), (5, 3), (4, 4)])
    # result = result.sort() # X -> sort()는 리스트에서만 사용 가능
    result = sorted(result.items()) # (등수, 참가번호) 기준으로 정렬
    result = result[:3]

    return 10000 * result[0][1] + 100 * result[1][1] + result[2][1]
