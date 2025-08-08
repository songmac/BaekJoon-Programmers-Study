def solution(myString, pat):
    new_str = ''
    for i in myString:
        if i == "A":
            i = i.replace("A", "B")
        elif i == "B":
            i = i.replace("B", "A")
        new_str += i
    result = new_str.find(pat)
    
    return 1 if result != -1 else 0