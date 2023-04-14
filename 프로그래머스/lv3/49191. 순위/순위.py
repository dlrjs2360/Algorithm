'''
순위를 매길 수 있다 == (내 앞의 사람의 수)+(내 뒤의 사람의 수) = (전체-1)
앞의 사람, 뒤의 사람을 모두 저장 -> 개수 비교
'''
from collections import defaultdict

def solution(n, results):
    answer = 0
    lose_dict = defaultdict(set) 
    win_dict = defaultdict(set)
    
    for a,b in results:
        win_dict[a].add(b)
        lose_dict[b].add(a)
        
    for i in range(1,n+1):         
        for winner in win_dict[i]:                    # i한테 진 애들은 i를 이긴 애들한테도 진 것
            lose_dict[winner].update(lose_dict[i])
        for loser in lose_dict[i]:                     # i한테 이긴 애들은 i한테 진 애들한테도 이긴 것
            win_dict[loser].update(win_dict[i])
    
    for i in range(1,n+1):
        if len(win_dict[i]) + len(lose_dict[i]) == n-1:   # i한테 이기고 진 애들 합쳐서 n-1이면 순위가 결정된 것
            answer += 1

    return answer