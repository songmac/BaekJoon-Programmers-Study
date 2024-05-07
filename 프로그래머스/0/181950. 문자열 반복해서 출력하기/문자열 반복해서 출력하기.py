str, n = input().strip().split(' ')
n = int(n)

for i in range(1, 5):
    result = str * n
    
print(result)

"""
input(): 사용자로부터 입력을 받은 것을 반환
.strip(): 이 메서드는 문자열의 앞뒤에 있는 공백(스페이스, 탭, 줄바꿈 등)을 제거
.split(' '): 이 메서드는 문자열을 인수로 주어진 구분자(' ' 공백)에 따라 분리하여 리스트를 만듬
"""