def ancestor(node):
    if node != parent[node]: parent[node] = ancestor(parent[node])
    return parent[node]

n,m,k = map(int,input().split())
fee = [0]+list(map(int,input().split()))
parent = [i for i in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    aa,ab = ancestor(a), ancestor(b)
    if aa == ab: continue
    if fee[aa] > fee[ab]: aa,ab = ab,aa
    parent[ab] = aa

for i in range(n+1):
    ancestor(i)

total = sum(fee[x] for x in set(parent))
print("Oh no" if total > k else total)