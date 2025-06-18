str = list(input())
num = len(str)
# print(num)

if 1 < num <= 20:
    for i in range (num):
        if str[i].isupper():
            str[i] = str[i].lower()
            print(str[i], end='')
        elif str[i].islower() :
            str[i] = str[i].upper()
            print(str[i], end='')
        else:
            print()