def solution(picks, minerals):
    
    graph =[[1,1,1],
            [5,1,1],
            [25,5,1]] 
    
    def mineralNum(s):
        if s == "diamond":
            return 0
        if s == "iron":
            return 1
        if s == "stone":
            return 2
        
    def DFS(cnt,prePick,total):
        nonlocal answer,picks
        
        if cnt >= len(minerals):
            answer = min(answer,total)
            return
        
        mNum = mineralNum(minerals[cnt])
        
        if (cnt+1) % 5 == 0:
            if picks.count(0) == 3:
                answer = min(answer,total+graph[prePick][mNum])
                return
            for pick in range(len(picks)):
                if picks[pick] > 0:
                    picks[pick] -= 1
                    DFS(cnt+1, pick, total+graph[prePick][mNum])
                    picks[pick] += 1
            return
        else:
            DFS(cnt+1, prePick, total+graph[prePick][mNum])
            
    answer = 1e9
    for pick in range(len(picks)):
        if picks[pick] > 0:
            picks[pick] -= 1
            DFS(0,pick,0)
            picks[pick] += 1
    
    return answer