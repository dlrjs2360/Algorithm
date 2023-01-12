import sys
sys.setrecursionlimit(10**7)

T = int(input())
for _ in range(T):
    n = int(input())

    parent = [0] * (n + 1)
    for _ in range(n-1):
        a,b = map(int,input().split())
        parent[b] = a

    x,y = map(int, input().split())
    y_parent = [y]

    node = y
    while 1:
        parent_node = parent[node]
        if parent_node == 0:
            break
        y_parent.append(parent_node)
        node = parent_node

    if x in y_parent:
        answer = x
    else:
        answer = 0
        node = x
        while 1:
            parent_node = parent[node]
            if parent_node in y_parent:
                answer = parent_node
                break
            node = parent_node

    print(answer)