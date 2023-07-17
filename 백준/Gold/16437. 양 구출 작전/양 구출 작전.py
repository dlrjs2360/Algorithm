import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
island, edges = [0] * (n+1), [[] for _ in range(n+1)]

for i in range(2,n+1):
    t,a,p = input().split()
    a,p = int(a),int(p)
    island[i] = a if t == 'S' else -a
    edges[i].append(p)
    edges[p].append(i)
edges[1].clear()

leaf = deque()
for k,v in enumerate(edges):
    if len(v) != 1: continue
    leaf.append(k)

while leaf:
    node = leaf.popleft()
    if len(edges[node]) != 1 or node == 1: continue
    nextNode = edges[node].pop()
    if island[node] > 0:
        island[nextNode] += island[node]
        island[node] = 0
    if nextNode != 1: edges[nextNode].remove(node)
    if len(edges[nextNode]) == 1: leaf.append(nextNode)

print(island[1])