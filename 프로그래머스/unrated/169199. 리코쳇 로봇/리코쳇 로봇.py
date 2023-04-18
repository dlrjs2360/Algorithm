from collections import deque

def slide(i,x,y,lx,ly,board):
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    while 1:
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < lx and 0 <= ny < ly) or board[nx][ny] == 'D':
            return x,y
        x,y = nx,ny

def solution(board):
    answer = -1
    lx,ly = len(board),len(board[0])
    
    robot = ()
    for i in range(lx):
        for j in range(ly):
            if board[i][j] == 'R':
                robot = (i,j)
    
    visit = [[False] * ly for _ in range(lx)]
    visit[robot[0]][robot[1]] = True
    q = deque([(robot[0],robot[1],0)])
    
    while q:
        x,y,cnt = q.popleft()
        if board[x][y] == 'G':
            answer = cnt
            break
        for i in range(4):
            nx,ny = slide(i,x,y,lx,ly,board)
            if not visit[nx][ny]:
                visit[nx][ny] = True
                q.append((nx,ny,cnt+1))
    return answer