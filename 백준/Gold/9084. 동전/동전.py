for _ in range(int(input())):
    n = int(input())
    coin = list(map(int,input().split()))
    target = int(input())
    dp = [0] * (target+1)

    for c in coin:
        if target >= c:
            dp[c] += 1
        for num in range(c+1,target+1):
            dp[num] += dp[num-c]

    print(dp[target])