def solution(money):
    coffee_value = 5500
    cup = money // coffee_value
    money_change = money % coffee_value
    return [cup, money_change]