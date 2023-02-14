import sys
input = sys.stdin.readline

def belman_ford(start):
    dist[start] = 0
    for i in range(1,n+1):
        for j in range(m):
            now, next, weight = graph[j]
            if dist[now] != 1e9 and dist[next] > dist[now] + weight:
                dist[next] = dist[now] + weight
                if i == n: return True
    return False

n, m = map(int,input().split())
graph = []
dist = [1e9] * (n+1)
for _ in range(m):
    graph.append(list(map(int,input().split())))

if belman_ford(1):
    print(-1)
else:
    for i in range(2,n+1):
        if dist[i] == 1e9:
            print(-1)
            continue
        print(dist[i])
        