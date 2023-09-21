import sys
input = sys.stdin.readline
from heapq import heappush,heappop

def ancestor(node):
    if node != parent[node]: parent[node] = ancestor(parent[node])
    return parent[node]

P,W = map(int, input().split())
C,V = map(int,input().split())
heap = []
for _ in range(W):
    a,b,c = map(int,input().split())
    heappush(heap,(-c,a,b))

answer = 1e9
parent = list(range(P))
while parent[C] != parent[V] and heap:
    c,a,b = heappop(heap)
    aa,bb = ancestor(a),ancestor(b)
    if aa == bb: continue
    answer = min(answer,-c)
    if aa > bb: parent[aa] = bb
    else: parent[bb] = aa

    for i in range(P):
        ancestor(i)

print(answer)