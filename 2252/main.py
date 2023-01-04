import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path+'/input.txt', "r")


from collections import deque

n, m = map(int,input().split())

# 그래프와 우선순위 결정
graph = [[] for _ in range(n+1)]
degree = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

# 0순위 입력받기
Q = deque()
for i,x in enumerate(degree):
    if i != 0 and x == 0:
        Q.append(i)

# 위상정렬
while Q:
    node = Q.popleft()
    print(node, end=" ")
    for x in graph[node]:
        degree[x] -= 1
        if degree[x] == 0:
            Q.append(x)
