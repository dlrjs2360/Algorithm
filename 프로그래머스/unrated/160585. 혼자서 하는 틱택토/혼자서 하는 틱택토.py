'''
- [x] X가 O보다 많으면 에러
- [] X가 O와 같은데 O가 한 줄을 완성했으면 에러
- [] X나 O가 여러 개의 줄을 이루었다면 에러( 단, 한 점으로 여러 줄을 완성한 것은 제외 )
'''

def solution(board):
    answer = -1
    l = 3 # 보드의 길이
    cntO, cntX = 0, 0
    O,X = [],[]
    for i in range(l):
        for j in range(l):
            if board[i][j] == "O": cntO += 1; O.append((i,j))
            elif board[i][j] == "X":  cntX += 1; X.append((i,j))

    if cntX > cntO: return 0

    visitO, visitX = [[False] * l for _ in range(l)], [[False] * l for _ in range(l)]
    answer = 0
    
    checkArr = [
        [(0,0),(1,1),(2,2)],
        [(0,0),(0,1),(0,2)],
        [(0,0),(1,0),(2,0)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],
        [(0,2),(1,1),(2,0)]
    ]
    
    def check(graph):
        for i in range(8):
            if sum(graph[x][y] for x,y in checkArr[i]) == l: return True
        return False
    
    def DFS(rO,rX,turn):
        nonlocal answer
        if answer: return
        if (check(visitO) and rX > 0) or (check(visitX) and rO > 0): return
        if rO == rX == 0: answer += 1; return
        if turn == "O":
            if rO == 0: return
            for i in range(cntO):
                cx,cy = O[i]
                if visitO[cx][cy]: continue
                visitO[cx][cy] = True
                DFS(rO-1,rX,"X")
                visitO[cx][cy] = False
        else:
            if rX == 0: return
            for i in range(cntX):
                cx,cy = X[i]
                if visitX[cx][cy]: continue
                visitX[cx][cy] = True
                DFS(rO,rX-1,"O")
                visitX[cx][cy] = False
    
    DFS(cntO,cntX,"O")
    
    return 1 if answer else 0