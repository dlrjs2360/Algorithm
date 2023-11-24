'''
직선: 100원
코너: 600원

n = 3 ~ 25

다익스트라로 최단거리를 구할 수 있음.
DP로 최단거리를 구하는 시간을 줄일 수 있음.
그 중 코너에서는 금액을 더할 수 있음.

방향이 다른 상황에서는 dp가 낮아도 된다.
'''

from collections import deque
from heapq import heappush, heappop

def solution(board):
    
    def checkRange(x,y):
        return 0 <= x < N and 0 <= y < N
    
    answer = 1e9
    N = len(board)
    
    dp = [[[1e9] * 4 for _ in range(N)] for _ in range(N)]
    dp[0][0][0] = 0 # x,y 
    dp[0][0][1] = 0
    
    heap = []
    heappush(heap, (0,0,0,0)) # (비용,방향,x,y)
    heappush(heap, (0,1,0,0))
    
    dx,dy = [1,0,0,-1],[0,1,-1,0]
    
    while heap:
        w,d,x,y = heappop(heap)
        
        if x == N-1 and y == N-1:
            answer = w
            break
            
        if dp[x][y][d] < w:
            continue
        
        for i in range(4):
            nw = w + (100 if i == d else 600)
            
            if nw >= answer: continue
            
            nx,ny = x+dx[i], y+dy[i]
            
            if not checkRange(nx,ny) or dp[nx][ny][i] <= w or board[nx][ny] == 1:
                continue
                
            dp[nx][ny][i] = nw
            heappush(heap,(nw,i,nx,ny))
    
    return answer