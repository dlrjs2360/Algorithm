import heapq, sys
input = sys.stdin.readline
n = int(input())
maxHeap, minHeap = [],[]
mid = int(input())
print(mid)
for _ in range(1,n):
    num = int(input())
    # mid보다 작다면 maxHeap, 크다면 minHeap에 넣는다.
    heapq.heappush(maxHeap,-num) if num < mid else heapq.heappush(minHeap,num)

    # mid의 값을 길이가 더 짧은 쪽으로 넣어준다.
    heapq.heappush(maxHeap, -mid) if len(maxHeap) < len(minHeap) else heapq.heappush(minHeap, mid)

    # 두 힙의 길이가 같다면 두 힙의 첫 번째 원소들 중 작은 것을 출력한다.
    if len(maxHeap) == len(minHeap):
        mid = heapq.heappop(minHeap) if -maxHeap[0] > minHeap[0] else -heapq.heappop(maxHeap)
    # 두 힙의 길이가 다르다면 더 긴 쪽 가장 앞의 원소를 출력한다.
    else:
        mid = -heapq.heappop(maxHeap) if len(maxHeap) > len(minHeap) else heapq.heappop(minHeap)

    print(f"{mid}")