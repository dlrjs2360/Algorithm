from collections import defaultdict

def solution(weights):
    answer = 0
    count = defaultdict(int)
    for w in weights:
        for i in [1, 2, 2/3, 3/2 ,3/4, 4/3, 2/4]:
            answer += count[w*i]
        count[w] += 1
            
    return answer