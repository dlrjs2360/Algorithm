import sys
input = sys.stdin.readline
from heapq import heappop,heappush
N = int(input())
count, computer = 0, []
heap = []
man = sorted([list(map(int,input().split())) for _ in range(N)])

# 초기값 설정
count += 1
heappush(heap, [man[0][1], 0]) # (end, idx)
computer.append(1)

done = []
for s,e in man[1:]:
    while heap and heap[0][0] < s:
        heappush(done,heappop(heap)[1])
    if done:
        idx = heappop(done)
        heappush(heap, [e, idx])
        computer[idx] += 1
    else:
        heappush(heap, [e, len(computer)])
        computer.append(1)
        count += 1

print(count)
print(*computer)