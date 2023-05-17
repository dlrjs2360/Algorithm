def copyMap(x,y):
    if graph[x][y] == 0:
        graph[x][y] = dice[2]
    else:
        dice[2] = graph[x][y]
        graph[x][y] = 0

n,m,x,y,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dice = [0]*6 # 왼쪽(0),오른쪽(1),바닥(2),출력(3),위(4),아래(5)
idx = [[],[2,3,1,0,4,5],[3,2,0,1,4,5],[0,1,4,5,3,2],[0,1,5,4,2,3]]
for way in map(int,input().split()):
    if way == 1 and y+1 < m:
        y += 1
    elif way == 2 and y-1 >= 0:
        y -= 1
    elif way == 3 and x-1 >= 0:
        x -= 1
    elif way == 4 and x+1 < n:
        x += 1
    else: continue
    dice = [dice[i] for i in idx[way]]
    copyMap(x,y)
    print(dice[3])