import sys
input = sys.stdin.readline

def merge(left_val, right_val):
    return left_val + right_val
def query(node, start, end, left, right):
    if start <= left and right <= end:
        return stree[node]
    if right < start or end < left:
        return 0
    return merge(query(node*2,start,end,left,(left+right)//2), query(node*2+1,start,end,(left+right)//2+1,right))

def update(node, idx, val, left, right):
    if left == right == idx:
        stree[node] = val
        return val
    if left > idx or idx > right:
        return stree[node]
    stree[node] = merge(update(node*2,idx,val,left,(left+right)//2), update(node*2+1,idx,val,(left+right)//2+1,right))
    return stree[node]

def build(node,left,right):
    if left == right:
        stree[node] = arr[right]
        return stree[node]
    stree[node] = merge(build(node*2,left,(left+right)//2), build(node*2+1,(left+right)//2+1,right))
    return stree[node]

n,m,k = map(int,input().split())
arr = [int(input()) for _ in range(n)]
stree = [0] * (n*4+1)
build(1,0,n-1)
for _ in range(m+k):
    a,b,c = map(int,input().split())
    if a == 1: # b번째 수를 c로 바꾸기
        update(1,b-1,c,0,n-1)
    if a == 2: # b부터 c까지의 합을 구하기
        print(query(1,b-1,c-1,0,n-1))