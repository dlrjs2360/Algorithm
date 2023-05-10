from collections import defaultdict
from heapq import heappop,heappush

n = int(input())
item = defaultdict(list) # a를 사면 b를 살 수 있다.
depth = defaultdict(int)
allItem = set()

for _ in range(n):
    a,b = input().split()
    allItem.update({a,b})
    item[a].append(b)
    depth[b] += 1

zeroDepth = []
for x in allItem :
    if depth[x] == 0:
        heappush(zeroDepth,x)

popedItem, tmp = [],[]
while zeroDepth:
    popedItem.append(node := heappop(zeroDepth))
    for nextNode in sorted(item[node]):
        depth[nextNode] -= 1
        if depth[nextNode] == 0:
            heappush(tmp,nextNode)
    if not zeroDepth:
        if not tmp: break
        zeroDepth = tmp
        tmp = []

if len(popedItem) != len(allItem):
    print(-1)
else:
    for x in popedItem:
        print(x)