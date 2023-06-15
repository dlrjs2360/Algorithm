import sys
input = sys.stdin.readline

def visitAll(n):
    return sum(2**x for x in range(n))
def DFS(start,node,visit,total):
    global answer
    if node == start and visit == visitAll(n):
        answer = min(answer, total)
        return
    for nextNode in range(n):
        if not visit & (1 << nextNode) and dist[node-1][nextNode-1] > 0:
            DFS(start,nextNode,visit | (1 << nextNode), total+dist[node-1][nextNode-1])

n = int(input())
dist = [list(map(int,input().split())) for _ in range(n)]
answer = 1e9
DFS(1,1,0,0)
print(answer)