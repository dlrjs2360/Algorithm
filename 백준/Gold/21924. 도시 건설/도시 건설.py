import sys
input = sys.stdin.readline

def ancestor(node):
    if node != parent[node]:
        parent[node] = ancestor(parent[node])
    return parent[node]

n,m = map(int,input().split())
cost = sorted(list(list(map(int,input().split())) for _ in range(m)), key=lambda x: x[2])
parent = [x for x in range(n+1)]
answer,MAX_VALUE = 0,0
for a,b,c in cost:
    MAX_VALUE += c
    if (ra := ancestor(a)) != (rb := ancestor(b)):
        answer += c
        if ra > rb:
            parent[ra] = rb
        else:
            parent[rb] = ra

for node in range(1,n+1):
    parent[node] = ancestor(node)
    if parent[node] != 1:
        print(-1)
        break
else:
    print(MAX_VALUE-answer)
