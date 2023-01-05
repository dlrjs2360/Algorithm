import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path+'/input.txt', "r")

from collections import deque
n,k = map(int,input().split())
arr = list(map(int,input().split()))

count = 0 # 현재 남은 1의 갯수
Q = deque()
for i in range(n):
    x = arr[i]
    if x == 1:
        count += 1
        Q.append(i)

ans = 1000001
res = 0
if count < k:
    print(-1)
else:
    start = Q.popleft()
    end = start
    while start <= end <= n-1:
        L = end - start + 1

        if arr[end] == 1:
            res += 1

        #print(start,end, res)

        if res >= k:
            ans = min(ans,L)
            res -= 1

            count -= 1
            if count < k:
                break

            start = Q.popleft()

        end += 1

    print(ans)

