def solution(price, money, count):
    return max(sum([price * x for x in range(1,count+1)]) - money,0)