n = int(input())
parent = list(map(int, input().split()))
delNode = int(input())


def DFS(node):
    parent[node] = -2
    for i in range(n):
        if parent[i] == node:
            DFS(i)


DFS(delNode)

ans = 0
for i in range(n):
    if i not in parent and parent[i] != -2:
        ans += 1

print(ans)