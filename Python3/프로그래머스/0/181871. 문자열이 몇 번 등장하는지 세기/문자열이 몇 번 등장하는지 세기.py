def solution(myString, pat):
    new_lst = []
    while True:
        if myString.find(pat) == -1:
            break
        myString = myString[myString.find(pat)+1:]
        new_lst.append(myString)
    return len(new_lst)