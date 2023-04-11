n = int(input())
tree = list(map(int,str(input())))
x,y = map(int,input().split())

a,b = 0,0
inOut = [[0,0] for _ in range(n+1)]
parent = [0] * (n+1)
depth = [0] * (n+1)
prev, last = 0, 0
for i in range(1,2*n+1):
    status = tree[i-1]
    if status == 0: # 0은 도착지
        last += 1
        parent[last] = prev
        depth[last] = depth[prev]+1
        prev = last
        inOut[last][0] = i
    else: # 1은 출발지
        inOut[prev][1] = i
        prev = parent[prev]

    #print(f"i:{i}, prev:{prev}, last:{last}, status:{status}")

for i in range(1,n+1):
    if x in inOut[i]:
        a = i
    if y in inOut[i]:
        b = i

while depth[a] != depth[b]:
    if depth[a] > depth[b]:
        a = parent[a]
    else:
        b = parent[b]

while a != b:
    a = parent[a]
    b = parent[b]

print(*inOut[a])