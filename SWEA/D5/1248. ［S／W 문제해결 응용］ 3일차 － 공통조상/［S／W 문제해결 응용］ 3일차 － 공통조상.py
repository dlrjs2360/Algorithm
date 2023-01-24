def LCA(x,y):
    while depth[x] != depth[y]: # 깊이 맞춰주기
        if depth[x] > depth[y]:
            x = parent[x]
            continue
        y = parent[y]

    while x != y:
        x = parent[x]
        y = parent[y]
    return x

def getDepth(node, d):
    if node:
        depth[node] = d
        for child in graph[node]:
            getDepth(child,d+1)
    return

def getChidecount(node):
    Q = deque([node])
    count = 0
    while Q:
        child = Q.popleft()
        count += 1
        for x in graph[child]:
            Q.append(x)
    return count

from collections import defaultdict,deque
T = int(input())
for test_case in range(1,T+1):
    v,e,a,b = map(int,input().split())
    parent = [0] * (v+1)
    depth = [0] * (v+1)
    graph = defaultdict(list)
    arr = list(map(int,input().split()))
    for i in range(0,e*2,2):
        parent[arr[i+1]] = arr[i]
        graph[arr[i]].append(arr[i+1])

    getDepth(1,0)
    lca = LCA(a,b)
    child = getChidecount(lca)
    print(f"#{test_case} {lca} {child}")
