import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def union(a,b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
        return
    parent[b] = a
def find(node):
    if node != parent[node]:
        node = find(parent[node])
    return node

n,m = map(int,input().split())
parent = [i for i in range(n+1)]
knew_num, *knew_person = map(int,input().split())


if knew_num == 0:
    print(m)
else:
    knew_parent = sorted(knew_person)[0]
    for i in range(knew_num-1):
        a,b = knew_person[i],knew_person[i+1]
        union(a,b)

    parties = []
    for _ in range(m):
        num, *party = map(int,input().split())
        for i in range(num-1):
            a,b = party[i],party[i+1]
            union(a,b)
        parties.append(party)
        
    knew_parent = find(knew_parent)
    ans = 0
    for x in parties:
        for node in x:
            if find(node) == knew_parent:
                break
        else:
            ans += 1

    print(ans)