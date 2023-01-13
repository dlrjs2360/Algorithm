import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def DFS(node):
    global team

    visit[node] = True
    cycle.append(node)

    next_node = arr[node]

    if visit[next_node]:
        if next_node in cycle:
            team += cycle[cycle.index(next_node):]
        return
    else:
        DFS(next_node)

T = int(input())
for _ in range(T):
    n = int(input())
    arr = [0]+list(map(int,input().split()))
    visit = [False] * (n+1)
    team = []

    for x in range(1,n+1):
        if x == arr[x]:
            visit[x] = True
            team.append(x)

    for x in range(1,n+1):
        if not visit[x]:
            cycle = []
            DFS(x)


    print(n-len(team))