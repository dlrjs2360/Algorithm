from collections import deque

N = int(input())
graph = {i:[] for i in range(1,N+1)}
for _ in range(N):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cross = [i for i in range(1, N + 1) if len(graph[i]) >= 3]

if not cross:
    print(*([0] * N))
else:
    start = 0

    # 순환선에 포함되는 점 찾기
    leaf = [i for i in range(1,N+1) if len(graph[i]) == 1]
    queue = deque()
    queue.append([leaf[0], leaf[0], (1 << leaf[0])])
    while queue:
        node,prev,visit = queue.popleft()
        status = False
        for next in graph[node]:
            if visit & (1 << next):
                if prev != next:
                    start = next
                    status = True
                    break
                continue
            queue.append((next, node, visit|(1 << next)))
        if status: break

    inCircle = 0
    dist = [0] * (N + 1)

    queue = deque()
    queue.append((start, start, 1 << start)) # node, prev, visit

    # 순환선 찾기
    while queue:
        node, prev, visit = queue.popleft()
        check = False
        for next in graph[node]:
            if visit & (1 << next):
                if prev != start and next == start:
                    check = True
                    inCircle = visit
                    break
                continue
            queue.append((next,node,visit | (1 << next)))
        if check: break

    queue.clear()
    visit = [False] * (N+1)
    for x in cross:
        if not inCircle & (1 << x): continue
        visit[x] = True
        queue.append((x,0))

    # 지선 점 거리 구하기
    while queue:
        node, d = queue.popleft()
        for next in graph[node]:
            if visit[next] or inCircle & (1 << next): continue
            dist[next] = d + 1
            queue.append((next,d+1))
            visit[next] = True

    print(*dist[1:])
