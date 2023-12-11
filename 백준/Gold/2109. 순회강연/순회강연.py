from heapq import heappop, heappush

n = int(input())
heap = []
maxDay = 0
for idx in range(n):
    a,b = map(int,input().split())
    maxDay = max(b, maxDay)
    heappush(heap,(-a,b))

done = [0] * (maxDay+1)
while heap:
    p,d = heappop(heap)
    p *= -1
    prev = []
    for i in range(d,0,-1):
        if done[i] == 0:
            done[i] = p
            break
        elif done[i] < p:
            heappush(prev,(p,i))
    else:
        if not prev:
            continue
        done[heappop(prev)[1]] = d

print(sum(done))