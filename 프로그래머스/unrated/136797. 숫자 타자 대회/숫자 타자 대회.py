from heapq import heappop, heappush
def solution(numbers):
    
    dist = [
    [1, 7, 6, 7, 5, 4, 5, 3, 2, 3], 
    [7, 1, 2, 4, 2, 3, 5, 4, 5, 6], 
    [6, 2, 1, 2, 3, 2, 3, 5, 4, 5], 
    [7, 4, 2, 1, 5, 3, 2, 6, 5, 4], 
    [5, 2, 3, 5, 1, 2, 4, 2, 3, 5], 
    [4, 3, 2, 3, 2, 1, 2, 3, 2, 3], 
    [5, 5, 3, 2, 4, 2, 1, 5, 3, 2], 
    [3, 4, 5, 6, 2, 3, 5, 1, 2, 4], 
    [2, 5, 4, 5, 3, 2, 3, 2, 1, 2], 
    [3, 6, 5, 4, 5, 3, 2, 4, 2, 1], 
    ]
    
    L = len(numbers:=list(map(int,list(numbers))))
    dp = [[[1e9]*12 for _ in range(12)] for _ in range(L+1)] # dp[인덱스][왼손][오른손]
    queue = [(0,4,6)]
    dp[0][4][6] = 0
    hands = []
    while queue:
        idx,left,right = heappop(queue)
        
        if idx > L-1: 
            hands.append((left,right))
            continue
            
        number = numbers[idx]
        rightChange = dp[idx][left][right] + dist[right][number]
        leftChange = dp[idx][left][right] + dist[left][number]
        
        if right != number and dp[idx+1][number][right] > leftChange:
            dp[idx+1][number][right] = leftChange
            heappush(queue,(idx+1,number,right))
        
        if left != number and dp[idx+1][left][number] > rightChange:
            dp[idx+1][left][number] = rightChange
            heappush(queue,(idx+1,left,number))
    
    return min([dp[L][x][y] for x,y in hands])
