def solution(myStr):
    for cha in "abc":  # a, b, c가 차례로 들어감
        myStr = myStr.replace(cha, " ")
    return myStr.split() if myStr.strip() else ["EMPTY"]