def solution(my_strings, parts):
    
    result=''
    for i in range(len(my_strings)):
        s, e = parts[i]  # 리스트 인자 [x, y]를 각각 s, e에 할당연산자 통해 할당함
        # print(s, e)  
        # print(type(s), type(e)) # (int, int)
        for j in range(s, e+1, 1):
            result += my_strings[i][j]
            
    return result