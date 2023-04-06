from collections import Counter
from heapq import heappush,heappop
def solution(k, tangerine):
    count = Counter(tangerine)
    
    heap = []
    for x in count.items():
        heappush(heap,(x[1],x[0]))
    
    c = len(tangerine) - k
    while c > 0:
        s = heappop(heap)
        if s[0] > c:
            c = 0
            heappush(heap,(s[1],s[0]))
            break
        else:
            c -= s[0]
        
    return len(heap)