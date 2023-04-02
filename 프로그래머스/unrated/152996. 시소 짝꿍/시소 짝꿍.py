'''
1. 같은 몸무게끼리는 Combination으로 n(n-1)//2
2. 같은 몸무게 사람들끼리는 묶어서 명수 저장하기
    - A몸무게와 B몸무게가 수평을 이루면 A*B를 정답에 더하기
3. 크기순으로 정렬해서 내 뒤의 수들과만 비교하면 된다.
'''

from collections import defaultdict

def solution(weights):
    answer = 0
    count = defaultdict(int)
    for w in weights:
        for i in [1, 2, 2/3, 3/2 ,3/4, 4/3, 2/4]:
            answer += count[w*i]
        count[w] += 1
            
    return answer