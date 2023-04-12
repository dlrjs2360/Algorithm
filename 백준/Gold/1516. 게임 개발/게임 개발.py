from collections import defaultdict,deque

n = int(input())
time = [0] * (n+1)
count = [0] * (n+1)
preq = defaultdict(list)

q = deque()
for i in range(1,n+1):
    arr = list(map(int,input().split()))
    time[i] = arr[0]
    for x in arr[1:-1]:
        preq[x].append(i)
        count[i] += 1
    if count[i] == 0:
        q.append(i)

ans = time.copy()
while q:
    #print(ans)
    x = q.popleft()
    for y in preq[x]:
        count[y] -= 1
        ans[y] = max(ans[y],time[y]+ans[x])
        if count[y] == 0:
            q.append(y)


print(*ans[1:],sep='\n')