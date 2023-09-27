import sys
input = sys.stdin.readline

def BFS():
    answer = False
    MIN = 1e9
    queue = deque()
    queue.append((0,1,False,0))
    while queue:
        w,node,wasP,visit = queue.popleft()
        if w > MIN: continue
        if node == P: wasP = True
        elif node == V:
            if w > MIN: continue
            elif w == MIN: answer = wasP if not answer else answer
            else:
                answer = wasP
                MIN = w
            continue
        for nextNode, nw in edges[node]:
            if visit & (1 << nextNode): continue
            queue.append((w+nw, nextNode, wasP, visit | (1 << nextNode)))

    return "SAVE HIM" if answer else "GOOD BYE"

if __name__ == "__main__":
    from collections import defaultdict, deque
    V, E, P = map(int, input().split())
    edges = defaultdict(list)
    for _ in range(E):
        a, b, c = map(int, input().split())
        edges[a].append((b, c))
        edges[b].append((a, c))
    print(BFS())

