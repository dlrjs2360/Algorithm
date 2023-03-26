import sys
input = sys.stdin.readline

from collections import deque
def BFS(start):
    Q = deque([start])
    visit[start] = True
    while Q:
        pnode = Q.popleft()
        for nnode in graph[pnode]:
            if not visit[nnode]:
                visit[nnode] = visit[pnode] * -1
                Q.append(nnode)
            elif visit[nnode] == visit[pnode]:
                return False
    return True

k = int(input())
for _ in range(k):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    visit = [False for _ in range(v+1)]

    for _ in range(e):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1,v+1):
        if not visit[i]:
            ans = BFS(i)
            if not ans:
                print("NO")
                break
    else:
        print("YES")