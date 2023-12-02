
for _ in range(int(input())):
    N,M = map(int,input().split())

    edgeCounter = {i: 0 for i in range(1,N+1)}
    edge = {i: list() for i in range(1,N+1)}
    bomb = [[0] * (N+1) for _ in range(N+1)]

    for _ in range(M):
        a,b,d = map(int,input().split())

        edgeCounter[a] += 1
        edgeCounter[b] += 1

        edge[a].append(b)
        edge[b].append(a)

        bomb[a][b] = d
        bomb[b][a] = d

    def dfs(node, prev, visit):
        res = 0
        for next in edge[node]:
            if visit & (1 << next): continue
            if bomb[node][next] == 1: res += 1
            else: res += dfs(next, node, visit | (1 << next))
        return min(bomb[node][prev],res) if res > 0 else bomb[node][prev]

    print(sum(dfs(node,1, 2 | (1 << node)) for node in edge[1]))
