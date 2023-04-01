def calTime(nexTime,preTime):
    preH, preM = map(int,preTime.split(":"))
    nexH, nexM = map(int,nexTime.split(":"))
    return (nexH-preH)*60 + (nexM-preM)

def solution(plans):
    answer = []
    stoped = []
    plans.sort(key = lambda x: list(map(int,x[1].split(":"))), reverse=True)
    while plans or stoped:
        name, start, pTime = plans.pop() if plans else stoped.pop()
        pTime = int(pTime)
        if plans:
            nex = plans[-1]
            diff = calTime(nex[1],start)
            if pTime > diff:
                stoped.append([name,start,pTime-diff])
                continue
            else:
                answer.append(name)
                if diff > pTime:
                    rest = diff - pTime
                    while rest > 0 and stoped:
                        sn,ss,sp = stoped.pop()
                        if rest >= sp:
                            rest -= sp
                            answer.append(sn)
                        else:
                            sp -= rest
                            stoped.append([sn,ss,sp])
                            break
        else:
             answer.append(name)          
        
         
    return answer