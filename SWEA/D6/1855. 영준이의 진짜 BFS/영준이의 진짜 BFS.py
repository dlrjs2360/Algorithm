def lca(a, b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]
    return a

from collections import defaultdict, deque
T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    graph = defaultdict(list)
    depth = defaultdict(int)
    parent = [0,0] + arr
    depth[1] = 0

    for i,x in enumerate(arr):
        depth[i+2] = depth[x]+1
        graph[x].append(i+2)

    answer,preNode = 0,1
    Q = deque([1])
    visit = [False] * (n + 2)
    visit[1] = True
    tmp = 0

    while Q:
        node = Q.popleft()
        if node != 1:
            tmp = (depth[node] + depth[preNode] - 2 * depth[lca(node,preNode)])
            answer += tmp

        #print("현재노드:",node,"부모노드:",preNode," 가중치:",tmp," 누적:",answer)

        for next_node in graph[node]:
            if not visit[next_node]:
                visit[next_node] = True
                Q.append(next_node)

        preNode = node

    print("#"+str(test_case),answer)