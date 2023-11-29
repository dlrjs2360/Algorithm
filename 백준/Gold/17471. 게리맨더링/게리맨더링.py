import sys
input = sys.stdin.readline
from collections import deque

def toBinary(num): return 1 << num
def toList(num): return list(x for x in range(1,N+1) if num & (1 << x))

def sumPeople(arr): return sum(people[x] for x in arr)

def checkLink(B):
    bList = toList(B)
    link = {b:False for b in bList}
    link[bList[0]] = True
    queue = deque()
    queue.append(bList[0])
    while queue:
        node = queue.popleft()
        for next in near[node]:
            if next not in bList or link[next]:
                continue
            link[next] = True
            queue.append(next)
    return all(link.values())

N = int(input())
people = [0]+list(map(int,input().split()))
near = {i:list() for i in range(1,N+1)}
for i in range(1,N+1):
    M, *arr = map(int,input().split())
    near[i] = arr

allVisit = sum(toBinary(x) for x in range(1,N+1))
allPeople = sum(people)
visit = [[False] * (allVisit+1) for _ in range(allVisit+1)]
answer = 1e9
for A in range(1,N+1):
    queue = deque()
    queue.append([ba := toBinary(A),bb := (allVisit - ba)]) # (A,B)
    visit[ba][bb] = True
    while queue:
        a,b = queue.popleft()
        if b == 0: continue
        if checkLink(b):
            answer = min(answer,abs(sumPeople(toList(a)) - sumPeople(toList(b))))
        for inA in toList(a):
            for next in near[inA]:
                if a & (1 << next) or visit[(na := (a+toBinary(next)))][(nb := (b-toBinary(next)))]: continue
                if (sumPeople(toList(na)) + sumPeople(toList(nb))) != allPeople:
                    continue
                queue.append((na,nb))
                visit[na][nb] = True

print(answer if answer < 1e9 else -1)