from collections import defaultdict, deque

def solution(edges):
    inList = defaultdict(list)
    outList = defaultdict(list)
    created, donut, stick, eight = -1,0,0,0
    
    
    for a,b in edges:
        outList[a].append(b)
        inList[b].append(a)
    
    # 생성점 찾기
    for x in outList.keys():
        if len(inList[x]) == 0 and len(outList[x]) > 1:
            created = x
            break
    
    visit = [False] * 1000001
    visit[created] = True
    
    # BFS로 그래프 종류 파악하기
    for x in outList[created]:
        queue = deque()
        queue.append(x)
        visit[x] = True
        nodeCnt, edgeCnt = 1,-1
        
        while queue:
            node = queue.popleft()
            edgeCnt += len(outList[node]) + len(inList[node])
            
            for nx in outList[node]:
                if visit[nx]: continue
                queue.append(nx)
                visit[nx] = True
                nodeCnt += 1
                
            for nx in inList[node]:
                if visit[nx]: continue
                queue.append(nx)
                visit[nx] = True
                nodeCnt += 1
        
        edgeCnt = edgeCnt // 2
        
        if nodeCnt == edgeCnt: donut += 1
        elif nodeCnt == edgeCnt+1: stick += 1
        else: eight += 1
        
    return [created, donut, stick, eight]