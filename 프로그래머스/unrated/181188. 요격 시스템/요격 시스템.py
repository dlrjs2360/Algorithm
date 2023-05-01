def solution(targets):
    answer = 0
    targets.sort()
    end = targets[0][1]
    for s,e in targets[1:]:
        if s >= end: # 떨어진 경우
            answer += 1
            end = e
        elif e <= end: # 포함된 경우
            if e < end:
                end = e
    return answer+1