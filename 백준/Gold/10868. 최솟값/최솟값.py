import sys
input = sys.stdin.readline
def build(node,left,right):
    if left == right:
        stree[node] = arr[left]
        return stree[node]
    mid = (left+right)//2
    stree[node] = min(build(node*2,left,mid), build(node*2+1,mid+1,right))
    return stree[node]

def query(node,start,end,left,right):
    if left > end or right < start: # 현재 구간이 겹치지 않는다면
        return int(1e9)
    if start <= left and right <= end:
        return stree[node]
    mid = (left+right)//2
    return min(query(node*2,start,end,left,mid), query(node*2+1,start,end,mid+1,right))

n,m = map(int,input().split())
arr = [int(input()) for _ in range(n)]
stree = [1e9] * (n*4)
build(1,0,n-1)
for _ in range(m):
    a,b = map(int,input().split())
    print(query(1,a-1,b-1,0,n-1))