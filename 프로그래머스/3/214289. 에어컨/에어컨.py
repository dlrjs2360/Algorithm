def solution(temperature, t1, t2, a, b, onboard):
    temp = temperature + 10 # 온도 범위 0~50로 수정
    t1 += 10
    t2 += 10
    if t1>temp: # 실외온도가 범위보다 높게 통일
        temp = (t1-temp) + t2
    #1일때 t1<temp<t2
    # 온도를 내림 a
    # 온도를 유지하면 b
    # 끄면 0 (온도 올라감)
    # 희망온도는 신경안써도됨.

    dp = [[1e9]*100 for _ in range(len(onboard))]
    dp[0][temp] = 0
    for i in range(1, len(onboard)):
        start = 0
        end = 0
        if onboard[i]==1:
            start = t1
            end = t2
        else:
            start = t1
            end = temp
        for j in range(start, end+1):
            if j==temp:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]+a)
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+b, dp[i-1][j+1]+a)
    return min(dp[len(onboard)-1])