import sys
input = sys.stdin.readline

def ancestor(node):
    parent[node] = ancestor(parent[node]) if parent[node] != node else node
    return parent[node]

v, e = map(int,input().split())
cost = sorted([list(map(int,input().split())) for _ in range(e)], key=lambda x:x[2])
parent = [i for i in range(v + 1)]

answer = 0
for a,b,c in cost:
    parent_a, parent_b = ancestor(a), ancestor(b)
    if parent_a != parent_b:
        answer += c
        if parent_a > parent_b:
            parent[parent_a] = b
            continue
        parent[parent_b] = a

print(answer)