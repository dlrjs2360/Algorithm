import sys
input = sys.stdin.readline
from collections import deque, defaultdict

dx,dy,dh = [1,0,0,-1,0,0],[0,1,-1,0,0,0],[0,0,0,0,1,-1]

while 1:
    l,r,c = map(int,input().split())
    if l == r == c == 0: break
    S,E = [],[]
    graph = defaultdict(list)
    for h in range(l):
        for f in range(r):
            arr = list(input())
            for i in range(c):
                if len(S) > 0 and len(E) > 0 : break
                if arr[i] == 'S': S = [h,f,i]
                elif arr[i] == 'E': E = [h,f,i]
            graph[h].append(arr)
        blank = input()

    queue = deque([(0,S)])
    visit = [[[False] * c for _ in range(r)] for _ in range(l)]
    visit[S[0]][S[1]][S[2]] = True
    answer = 0

    while queue:
        time ,node = queue.popleft()
        h,x,y = node
        if list(node) == E:
            print("Escaped in " + str(time) + " minute(s).")
            break
        for i in range(6):
            nh, nx, ny = h+dh[i], x+dx[i], y+dy[i]
            if nh < 0 or nh >= l or nx < 0 or nx >= r or ny < 0 or ny >= c: continue
            if visit[nh][nx][ny] or graph[nh][nx][ny] == '#': continue
            queue.append([time+1,(nh,nx,ny)])
            visit[nh][nx][ny] = True
    else:
        print("Trapped!")