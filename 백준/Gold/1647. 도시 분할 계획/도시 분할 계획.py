import sys
input = sys.stdin.readline

def ancestor(node):
    if parent[node] != node:
        parent[node] = ancestor(parent[node])
    return parent[node]

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(m)]
parent = [x for x in range(n+1)]
maxv = 0
s = 0
for a,b,c in sorted(graph, key=lambda x: x[2]):
    pa, pb = ancestor(a),ancestor(b)
    if pa != pb:
        s += c
        maxv = max(maxv,c)
        if pa > pb:
            parent[pa] = b
        else:
            parent[pb] = a

print(s-maxv)