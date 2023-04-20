'''
- 이모티콘 별로 할인율이 10,20,30,40이 들어갈 수 있음.
- 이모티콘 할인율들이 정해지면 유저가 탐색하여 정답 갱신
- 7개의 이모티콘에 4개의 할인율이 모두 담긴 배열을 생성 -> 4**7
'''
from itertools import product

def getPrice(emoticons,ratio,userRate):
    tmp = 0
    for i in range(len(emoticons)):
        if ratio[i] >= userRate:
            tmp += emoticons[i]*(100-ratio[i])//100
    return tmp

def solution(users, emoticons):
    answer = []
    lu,le = len(users), len(emoticons)
    arr = [10,20,30,40]
    for ratio in product(arr,repeat = le):
        membership,total = 0,0
        for user in users:
            if (res:=getPrice(emoticons,ratio,user[0])) >= user[1]:
                membership += 1
            else:
                total += res
        answer.append([membership,total])
    
    return sorted(answer,reverse = True)[0]