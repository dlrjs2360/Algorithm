from collections import deque
def solution(n, wires):
    answer = 100
    for i in range(n-1):
        wire = wires.copy()
        tmp = wire.pop(i)
        q1,q2 = deque([tmp[0]]),deque([tmp[1]])
        ch1,ch2 = [tmp[0]],[tmp[1]]
        dic = {x:[] for x in range(1,n+1)}
        for x in wire:
            dic[x[0]].append(x[1])
            dic[x[1]].append(x[0])
        while(q1):
            cm1 = q1.popleft()
            for j in dic[cm1]:
                if j not in ch1:
                    q1.append(j)
                    ch1.append(j)
        while(q2):
            cm2 = q2.popleft()
            for j in dic[cm2]:
                if j not in ch2:
                    q2.append(j)
                    ch2.append(j)
        ln1,ln2 = len(ch1),len(ch2)
        print(ch1,ch2)
        answer = min(abs(ln2-ln1),answer)
    return answer