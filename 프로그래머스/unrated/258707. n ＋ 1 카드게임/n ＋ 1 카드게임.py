from collections import deque

def solution(coin, cards):
    n = max(cards)
    m = n+1
    
    cards = deque(cards)   
    
    passed = [False] * m
    have = [False] * m
    for x in [cards.popleft() for _ in range(n//3)]:
        have[x] = True
    
    round = 1
    
    while cards:
        status = False
        
        for _ in range(2): passed[cards.popleft()] = True
            
        for i,v in enumerate(have): # 손에 있는 카드를 반드시 사용
            if not v: continue
            if have[m-i]: # 손에 있는 카드들로 해결
                have[i] = False
                have[m-i] = False
                status = True
                break
            elif passed[m-i] and coin > 0: # 지나간 카드 1, 손에 있는 카드 1
                have[i] = False
                passed[m-i] = False
                coin -= 1
                status = True
                break
        else: # 손에 있는 카드 없이 사용
            if coin >= 2:
                for i,v in enumerate(passed):
                    if not v: continue
                    if passed[m-i]:
                        coin -= 2
                        status = True
                        passed[i] = False
                        passed[m-i] = False
                        break
                    
        if not status: break
        else: round += 1
                
    
    return round