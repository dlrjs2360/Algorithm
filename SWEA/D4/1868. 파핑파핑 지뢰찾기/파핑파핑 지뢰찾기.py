def check(x,y):
    for h in range(8):
        nx = x+dx[h]
        ny = y+dy[h]
        if not (0 <= nx < n) or not (0 <= ny < n):
            continue
        if graph[nx][ny] == "*":
            return -1
    return 0

def click(x, y):
    next_click = []
    for h in range(8):
        nx, ny = x+dx[h], y+dy[h]
        if (0 <= nx < n) and (0 <= ny < n) and graph[nx][ny] == ".":
            graph[nx][ny] = check(nx,ny)
            if graph[nx][ny] == 0:
                next_click.append((nx,ny))

    for xx,yy in next_click:
        click(xx,yy)

T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    graph = []
    for _ in range(n):
        s = input()
        graph.append(list(s))

    dx = [1,1,1,0,0,-1,-1,-1]
    dy = [1,0,-1,1,-1,1,0,-1]

    answer = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "." and check(i,j) == 0:
                graph[i][j] = 0
                answer += 1
                click(i,j)

    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '.':
                cnt += 1

    print(f"#{test_case} {answer+cnt}")