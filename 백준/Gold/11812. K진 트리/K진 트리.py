import sys
input = sys.stdin.readline

def getDepth(node):
    i,cnt = 0,0
    while 1:
        cnt += k**i
        if cnt >= node:
            return i
        i += 1

def getParent(node):
    return (node-2)//k + 1

def LCA(x,y):
    if getDepth(x) != getDepth(y):
        while getDepth(x) != getDepth(y):
            if getDepth(x) > getDepth(y):
                x = getParent(x)
                continue
            y = getParent(y)
    while x != y:
        x = getParent(x)
        y = getParent(y)
    return x

n,k,q = map(int,input().split())
for _ in range(q):
    x,y = map(int,input().split())
    if k == 1:
        print(abs(x-y))
        continue
    print(getDepth(x) + getDepth(y) - 2 * getDepth(LCA(x,y)))