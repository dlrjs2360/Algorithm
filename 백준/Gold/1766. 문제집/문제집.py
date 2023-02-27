import heapq
n,m = map(int,input().split())

first = [[] for _ in range(n+1)]
link = [0 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    first[a].append(b)
    link[b] += 1

hq = []
for i in range(1,n+1):
    if link[i] == 0:
        heapq.heappush(hq,i)

while hq:
    node = heapq.heappop(hq)
    print(node, end=" ")
    for x in first[node]:
        link[x] -= 1
        if link[x] == 0:
            heapq.heappush(hq,x)