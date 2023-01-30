import sys
input = sys.stdin.readline
def update(idx, num):
    while idx <= len(stree):
        stree[idx] += num
        idx += (idx & -idx)
def query(idx):
    ans = 0
    while idx > 0:
        ans += stree[idx]
        idx -= (idx & -idx)
    return ans

n,m,k = map(int,input().split())
arr = [0]+[int(input()) for _ in range(n)]

stree = [0] * (n*4+1)
for i in range(1,n+1):
    update(i,arr[i])

for _ in range(m+k):
    a,b,c = map(int,input().split())
    if a == 1:
        diff = c-arr[b]
        update(b,diff)
        arr[b] += diff
    if a == 2:
        print(query(c) - query(b-1))