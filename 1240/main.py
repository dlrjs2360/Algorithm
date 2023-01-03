import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path+'/input.txt', "r")

from collections import defaultdict, deque
n,m = map(int,input().split())
dis = [[0 for _ in range(n+1)] for _ in range(n+1)]
graph = defaultdict(list)

for _ in range(n-1):
    a,b,c = map(int,input().split())
    dis[a][b] = c
    dis[b][a] = c
    graph[a].append(b)
    graph[b].append(a)

for _ in range(m):
    start, goal = map(int,input().split())

    que = deque([(start, 0)])
    visit = set()
    while que:
        node, total = que.popleft()
        if node == goal:
            print(total)
            break
        for x in graph[node]:
            if x not in visit:
                visit.add(x)
                que.append((x,total+dis[node][x]))

