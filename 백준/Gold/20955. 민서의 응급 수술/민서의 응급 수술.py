import sys
input = sys.stdin.readline

def ancestor(node):
    if parent[node] != node:
        parent[node] = ancestor(parent[node])
    return parent[node]

N,M = map(int,input().split())
parent = [i for i in range(N+1)]

minus = 0
for _ in range(M):
    u,v = map(int,input().split())
    au,av = ancestor(u),ancestor(v)
    if au == av:
        minus -= 1
        continue
    if au > av: au,av = av,au
    parent[av] = au

for i in range(1,N+1):
    ancestor(i)

answer = set(parent)

print(len(answer)-2-minus)