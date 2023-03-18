import sys
input = sys.stdin.readline

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

n = int(input())
xlst, ylst, zlst = [],[],[]
for i in range(n):
    x,y,z = map(int,input().split())
    xlst.append((x, i))
    ylst.append((y, i))
    zlst.append((z, i))

xlst.sort()
ylst.sort()
zlst.sort()

edges = []
for lst in (xlst,ylst,zlst):
    for i in range(n-1):
        w1, a = lst[i]
        w2, b = lst[i+1]
        edges.append((abs(w1-w2),a,b))
edges.sort()

parent = [i for i in range(n)]
ans = 0
for w,a,b in edges:
    a, b = find(a),find(b)
    if a != b:
        if a > b:
            a,b = b,a
        parent[b] = a
        ans += w

print(ans)