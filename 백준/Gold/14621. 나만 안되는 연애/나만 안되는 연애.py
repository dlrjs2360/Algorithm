import sys
input = sys.stdin.readline

def ancestor(node):
    if parent[node] != node: parent[node] = ancestor(parent[node])
    return parent[node]

N,M = map(int,input().split())
school = ["X"]+list(input().split())
parent = [x for x in range(N+1)]
graph = sorted([list(map(int,input().split())) for _ in range(M)], key=lambda x:x[2])

answer = 0
for a,b,c in graph:
    aa, ab = ancestor(a),ancestor(b)
    if aa == ab or school[a] == school[b]: continue
    if aa > ab: aa,ab = ab,aa
    parent[ab] = aa
    answer += c

for x in range(1,N+1):ancestor(x)


print(answer if len(set(parent[1:])) == 1 else -1)