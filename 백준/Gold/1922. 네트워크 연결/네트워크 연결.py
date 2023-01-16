from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

cost = []
parent = defaultdict(int)
for _ in range(m):
    a,b,c = map(int,input().split())
    parent[a] = a
    parent[b] = b
    cost.append((c,a,b))
cost.sort()

def ancestor(node):
    parent[node] = ancestor(parent[node]) if parent[node] != node else node
    return parent[node]

answer = 0
for c,a,b in cost:
    if ancestor(a) != ancestor(b):
        answer += c
        parent[ancestor(b)] = a

print(answer)