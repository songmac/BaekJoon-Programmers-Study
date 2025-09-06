"""
# 리스트 사용
def solution(order):
    cold_americano = ["iceamericano", "americanoice", "americano", "anything"]
    hot_americano = ["hotamericano", "americanohot"]
    cold_caffelatte = ["icecafelatte", "cafelatteice", "cafelatte"]
    hot_caffelatte = ["hotcafelatte", "cafelattehot"]
    
    cnt1, cnt2 = 0, 0
    for i in order:
        if (i in cold_americano) or (i in hot_americano):
            cnt1 += 1
        elif (i in cold_caffelatte) or (i in hot_caffelatte):
            cnt2 += 1
    return 4500 * cnt1 + 5000 * cnt2
    """

# 딕셔너리 사용

def solution(order):
    price_map = {
        "iceamericano" : 4500,
        "americanoice" : 4500,
        "americano" : 4500,
        "anything" : 4500,
        "hotamericano" : 4500,
        "americanohot" : 4500,
        "icecafelatte" : 5000,
        "cafelatteice" : 5000,
        "cafelatte" : 5000,
        "hotcafelatte" : 5000,
        "cafelattehot" : 5000,
    }
    # price_map = dict(
    #     iceamericano = 4500, 
    #     ...
    # )
    
    total = 0
    for i in order:
        if i in price_map:
            total += price_map[i]
    
    return total
            