def bf():
    dis = [0] * (n + 1)
    for i in range(n):
        for way in graph:
            cur,next_node,cost = way
            if dis[next_node] > dis[cur] + cost:
                dis[next_node] = dis[cur] + cost
                if i >= n-1:
                    return False
    return True

for _ in range(int(input())):

    n,m,w = map(int,input().split())
    graph = []

    for _ in range(m):
        s,e,t = map(int,input().split())
        graph.append((s,e,t))
        graph.append((e,s,t))

    for _ in range(w):
        s,e,t = map(int,input().split())
        graph.append((s,e,-t))

    print("YES" if not bf() else "NO")