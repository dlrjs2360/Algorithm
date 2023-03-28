'''
4 4 / 3 3 / 2 4 가 있을 때 3 3과 2 4는 같은 합임에도 3 3은 4 4보다 모두 작아서 고과를 받지 못한다.
고과를 받지 못하는 인원 제외 -> 완호가 포함되면 -1 -> 완호보다 합이 큰 사람의 수 세기
n번 돌면서 두 수가 종합적으로 가장 큰 사람 찾기? -> 판단 불가능
점수별로 두 번 정렬해서 2n번 탐색으로 내 앞의 친구보다 작으면 제외?
    - 17 5 / 6 3 / 4 4 같은 경우라면? 내 앞보다는 큰 것도 있지만 내 앞앞보다는 모두 작다.
    - 두번째로 정렬하게 되면 5 17 / 4 4 / 3 6 이 되어서 일단 제외가 되긴 한다.
    - 모든 경우에서 되는지는 확인하기 어렵다.
+)
합, 첫번째, 두번째 를 기준으로 정렬한다면 내 바로 앞에 있는 친구와만 비교할 수 있을까?

'''

def solution(scores):
    
    ho = scores[0]
    sum_ho = sum(scores[0])
    
    scores.sort(key=lambda x: (-x[0],x[1]))
    
    answer = 0
    before = 0
    for score in scores:
        if ho[0] < score[0] and ho[1] < score[1]:
            return -1
        if before <= score[1]:
            if sum(score) > sum_ho:
                answer += 1
            before = score[1]
            
    return answer+1
    