from collections import defaultdict
def solution(info, edges):
    answer = 0
    childs = defaultdict(list)
    
    for a,b in edges:
        childs[a].append(b)
    
    # 양의 수, 늑대의 수, 위치
    def DFS(s,w,l,stack,visit):
        nonlocal answer
        answer = max(answer,s)
        for c in stack:
            if visit & (1 << c):
                continue
            if info[c] == 0:
                DFS(s+1,w,c,stack+childs[c],visit | (1 << c))
            elif s > w+1:
                DFS(s,w+1,c,stack+childs[c],visit | (1 << c))
    
    DFS(1,0,0,childs[0],1)
    
    return answer