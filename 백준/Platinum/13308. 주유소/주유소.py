import heapq,sys
input=sys.stdin.readline

n,m = map(int,input().split())
price = [0]+list(map(int,input().split()))

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a,b,w = map(int,input().split())
    graph[a].append([b, w])
    graph[b].append([a, w])

def dijkstra():
    dp = [[1e9] * (max(price)+1) for _ in range(n+1)]
    dp[1][price[1]] = 0
    Q = []
    heapq.heappush(Q,(0,price[1],1))
    while Q:
        now_dist, now_cost, now = heapq.heappop(Q)
        if now == n:
            return now_dist
        if dp[now][now_cost] < now_dist:
            continue
        for next, next_dist in graph[now]:
            next_cost = min(price[next],now_cost)
            if dp[next][now_cost] > now_dist + (now_cost * next_dist):
                dp[next][now_cost] = now_dist + (now_cost * next_dist)
                heapq.heappush(Q,(now_dist + (now_cost * next_dist), next_cost, next))

print(dijkstra())