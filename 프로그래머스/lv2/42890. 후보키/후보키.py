'''
컬럼은 최대 8개이기 때문에 모든 8개의 모든 조합을 저장해서 길이가 같다면 후보키다.
1. 몇 개의 컬럼을 조합할 지 결정한다.
2. 해당 컬럼의 개수대로 어떤 컬럼들을 묶을지 조합한다.
3. 모든 로우들을 탐색하며 값을 저장한다.
4. 길이가 같다면 후보키다.
5. 만약 이미 후보키인 조합을 포함한다면 최소성을 만족시키지 못하므로 후보키가 되지 못한다.
'''

from itertools import combinations
from collections import defaultdict
def solution(relation):
    answer = 0
    column, row = len(relation[0]),len(relation)
    dic = defaultdict(int)
    for i in range(1,column+1): #1 컬럼개수
        for x in combinations(range(column),i): #2 컬럼조합
            
            status = 0 #5 최소성 검사
            for h in range(1,len(x)):
                for y in combinations(x,h):
                    if dic[y]:
                        status = 1
                        break
            if status:
                continue
                
            res =[]
            for r in relation: #3 모든 로우 탐색
                tmp = []
                for j in x:
                    tmp.append(r[j])
                if tmp not in res:
                    res.append(tmp)
                    
            if len(res) == row: # 유일성 검사
                dic[x] = 1
                answer += 1
                
    return answer