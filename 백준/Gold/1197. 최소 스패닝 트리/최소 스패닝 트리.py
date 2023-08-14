import sys
input = sys.stdin.readline

from collections import defaultdict

def ancestor(node):
    if parent[node] != node:
        parent[node] = ancestor(parent[node])
    return parent[node]

V, E = map(int, input().split())
edges = sorted([list(map(int, input().split())) for _ in range(E)], key=lambda x: x[2], reverse=True)

answer = 0
parent = defaultdict(int)
for node in range(1,V+1):
    parent[node] = node
    
while edges:
    a, b, w = edges.pop()
    aa, ab = ancestor(a), ancestor(b)
    if aa == ab: continue
    answer += w
    if aa > ab: aa, ab = ab, aa
    parent[ab] = aa

print(answer)