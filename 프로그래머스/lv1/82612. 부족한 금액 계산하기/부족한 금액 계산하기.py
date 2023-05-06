def solution(price, money, count):
    answer = sum([price * x for x in range(1,count+1)]) - money
    return max(answer,0)