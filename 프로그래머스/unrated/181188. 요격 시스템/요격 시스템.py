'''
1. 현재 요격가능한 범위의 가장 짧은 범위를 저장 - a,b
2. (a,b)와 겹치는 범위가 있는 것들을 모두 한번에 처리
3. 정렬한 배열에서는 다음 미사일이 범위를 벗어나면 그 뒤의 미사일들도 범위를 벗어남.
'''

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