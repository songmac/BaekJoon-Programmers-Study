def solution(my_string, overwrite_string, s):
    a = len(my_string[:s])
    b = len(overwrite_string)
    answer = my_string[:s] + overwrite_string[:b] + my_string[a+b:]
    
    return answer


            
            