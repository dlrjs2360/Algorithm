from heapq import heappop,heappush
n = int(input())
arr = sorted([sorted(list(map(int,input().split()))) for _ in range(n)], key=lambda x: x[1])
d = int(input())
answer = 0
heap = []
for s,e in [(x,y) for x,y in arr if (y-x) <= d]:
    while heap and heap[0][0] < e-d:
        heappop(heap)
    heappush(heap,(s,e))
    answer = max(answer,len(heap))
print(answer)