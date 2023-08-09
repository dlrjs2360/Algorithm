import sys
input = sys.stdin.readline

from collections import defaultdict,deque

N, Q = map(int,input().split())
numbers = [0]+list(map(int,input().split()))

edges = defaultdict(list)
for _ in range(N-1):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)

for _ in range(Q):
    x,y = map(int,input().split())
    visit = [False] * (N+1)
    queue = deque()
    queue.append((numbers[x],x))
    visit[x] = True
    while queue:
        total, node = queue.popleft()
        if node == y: print(total); break
        for nextNode in edges[node]:
            if visit[nextNode]: continue
            visit[nextNode] = True
            queue.append((int(str(total)+str(numbers[nextNode])) % 1000000007,nextNode))