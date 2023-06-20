import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def ancestor(node):
    if node != parent[node]:
        parent[node] = ancestor(parent[node])
    return parent[node]

n,m = map(int,input().split())
parent = [x for x in range(n)]

answer = 0
for i in range(m):
    a,b = map(int,input().split())
    aa,ab = ancestor(a),ancestor(b)
    if aa == ab:
        answer = i+1
        break
    if a > b : a,b = b,a
    parent[ab] = aa

print(answer)