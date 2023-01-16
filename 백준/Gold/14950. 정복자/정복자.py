import sys
input = sys.stdin.readline

n,m,t = map(int,input().split())
roads = [list(map(int,input().split())) for _ in range(m)]
roads.sort(key=lambda x:x[2])
parent = [i for i in range(n+1)]


def ancestor(node):
    parent[node] = ancestor(parent[node]) if parent[node] != node else node
    return parent[node]

count = 0
answer = 0
for a,b,c in roads:
    parent_a, parent_b = ancestor(a), ancestor(b)
    if parent_a != parent_b:
        answer += c + (count*t)
        parent[ancestor(a)] = b
        count += 1

print(answer)