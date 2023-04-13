'''
플로이드 워샬로 모든 점에서 모든 지점으로 향하는 최단거리를 구한다.
(출발점 -> 특정지점) + (특정지점 -> A도착점) + (특정지점 -> B도착점)의 최소값을 구한다.
생각해볼 수 있는 경우는 다음과 같다.
1. A나 B가 가는 길에 B나 A가 중간에 내리는 경우 -> 탐색하다가 A나 B의 도착점이 있는지 확인
2. A와 B가 처음부터 다른 방향으로 가야하는 경우
3. A와 B가 함께 가다가 중간에 흩어지는 경우
그렇다면 어떤 점에서 다른 점으로 향하는 최단거리들을 구해 그 합이 최소인 것을 찾는다.
'''

def solution(n, s, a, b, fares):
    
    MAX = float("inf")
    dp = [[MAX] * (n+1) for _ in range(n+1)]
    for A,B,w in fares:
        dp[A][B] = w
        dp[B][A] = w    
    
    for i in range(1,n+1):
        dp[i][i] = 0 
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j])

    answer = 1e9      
    for x in range(1,n+1):
        if (res:=dp[x][a]+dp[x][b]+dp[s][x]) < answer:
            answer = res
    
    return answer