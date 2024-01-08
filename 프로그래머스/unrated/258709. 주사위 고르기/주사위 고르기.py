from itertools import combinations
from collections import defaultdict, Counter

def solution(dice):
    answer = []
    n = len(dice) // 2
    
    maxPercent = 0
    
    dice_count = defaultdict(Counter)
    for i,x in enumerate(dice):
        dice_count[i] = Counter(x)
    
    for d in combinations(range(len(dice)),n):
        me, op = defaultdict(int), defaultdict(int)
        # 한 사람이 가진 주사위로 만들 수 있는 값의 경우의 수를 구한다.
        # 그러기 위해서 주사위 개수에 따라 어떤 값들의 조화가 나올 수 있는지 파악한다.
        
        # 플레이어 주사위 경우의 수
        for x in d:
            if len(me.keys()) == 0:
                for v,c in dice_count[x].items():
                    me[v] = c
                continue
            tmp = defaultdict(int)
            for v1,c1 in me.items():
                for v2,c2 in dice_count[x].items():
                    tmp[v1+v2] += c1*c2
            me = tmp
            
        # 상대 주사위 경우의 수
        for x in [i for i in range(len(dice)) if i not in d]:
            if len(op.keys()) == 0:
                for v,c in dice_count[x].items():
                    op[v] = c
                continue
            tmp = defaultdict(int)
            for v1,c1 in op.items():
                for v2,c2 in dice_count[x].items():
                    tmp[v1+v2] += c1*c2
            op = tmp
            
        win, lose = 0,0
        for v1,c1 in me.items():
            for v2,c2 in op.items():
                if v1 > v2:
                    win += c1*c2
                else:
                    lose += c1*c2

        winPercent = win / (win+lose)
        
        if winPercent > maxPercent:
            answer = sorted([x+1 for x in d])
            maxPercent = winPercent
            
    return answer