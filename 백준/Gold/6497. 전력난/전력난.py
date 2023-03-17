import sys
input = sys.stdin.readline

def ancestor(node):
    parent[node] = ancestor(parent[node]) if parent[node] != node else node
    return parent[node]

while 1:
    m,n = map(int,input().split())
    if m == n == 0:
        break

    parent = [i for i in range(m)]
    road = []
    for _ in range(n):
        x,y,z = map(int,input().split())
        road.append((z,x,y))
    road.sort()

    res = 0
    for c,a,b in road:
        a, b = ancestor(a), ancestor(b)
        if a != b:
            if a < b:
                a,b = b,a
            parent[a] = b
            continue
        res += c

    print(res)
