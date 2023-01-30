T = int(input())
for test_case in range(1,T+1):
    n,k = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    dp = [[0] * (k+1) for _ in range(n+1)]
    for i in range(1,n+1): # 아이템의 종류
        for j in range(1,k+1): # 무게에 따른 탐색
            w = j - arr[i-1][0]
            if w >=0 :
                dp[i][j] = max(dp[i-1][j],arr[i-1][1]+dp[i-1][w])
                continue
            dp[i][j] = dp[i-1][j]

    print(f"#{test_case} {dp[-1][-1]}")