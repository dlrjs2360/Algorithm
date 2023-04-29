# 블럭 지우기
def destroy(board,m,n):
    dx,dy = [1,1,0],[0,1,1]
    res = []
    cnt = 0
    for x in range(m):
        for y in range(n):
            if board[x][y].isdecimal():
                continue
            tmp = []
            for i in range(3):
                nx,ny = x+dx[i],y+dy[i]
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == board[x][y]:
                    tmp.append((nx,ny))
                    continue
                break
            else:
                res += tmp+[(x,y)]

    for bx,by in res:
        if board[bx][by] != '0':
            cnt += 1
            board[bx][by] = '0'

    return (cnt,board)
    
# 블럭 채우기
def fall(n,m,board):
    for x in range(m-1,-1,-1):
        for y in range(n):
            if board[x][y].isdecimal():
                h = x
                while 0 < h:
                    if not board[h][y].isdecimal():
                        break
                    h -= 1
                board[x][y] = board[h][y]
                board[h][y] = '0'
    return board

def printBoard(board):
    for x in board:
        print(x)
    print()
    
def solution(m, n, board):
    answer = 0
    while 1:
        cnt,board = destroy(list(list(x) for x in board),m,n)
        if cnt == 0:
            break
        answer += cnt
        board = fall(n,m,board) 
            
    return answer