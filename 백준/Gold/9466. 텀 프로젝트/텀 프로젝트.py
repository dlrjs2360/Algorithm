import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(i):
    global team
    next = choice[i]
    if visit[next]:
        if next in cycle:
            team += cycle[cycle.index(next):]
        return
    else:
        visit[next] = True
        cycle.append(next)
        dfs(next)

visit = []

for _ in range(int(input())):
    n = int(input())
    choice = [-1] + list(map(int,input().split()))
    visit = [False] * (n + 1)
    team = []

    for i in range(1,n+1):
        if choice[i] == i:
            visit[i] = True
            team.append(i)

    for i in range(1,n+1):
        if visit[i]: continue
        cycle = []
        dfs(i)

    print(n - len(team))
