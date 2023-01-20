

'''
1. 그래프를 돌면서 1을 찾는다. -> queue or dfs
2. 1을 찾으면 네 방향을 모두 탐색하며 갈 수 있는 방향을 찾는다.
3. 갈 수 있는 방향을 찾으면 그 방향으로 전선을 연결하고 dfs를 실시한다.
4. 갈 수 있는 방향을 찾았을 때는 모두 1로 바꿔주고 작업이 완료되면 0으로 바꿔준다.
5. 남은 코어의 개수와 현재 연결된 코어의 개수의 합이 정답보다 작으면 dfs를 종료한다.
6. 남은 코어의 개수가 0이 되면 정답을 갱신한다.
'''

def dfs(core_index,precount,prelength):
    # 길이를 갱신해준다.
    if precount > answer[0]:
        answer[0], answer[1] = precount, prelength
    elif answer[0] == precount:
        answer[1] = min(answer[1],prelength)

    # 더이상 탐색할 코어가 없다면
    if core_index == core_count:
        return

    # 다음 코어 탐색하기
    core_x, core_y = core[core_index]
    for d in range(4):
        direction = check(core_x,core_y, d)
        if direction == 0:
            continue
        connect(core_x,core_y,d) # 연결하기
        dfs(core_index+1,precount+1,prelength+direction)
        connect(core_x,core_y,d) # 다시 연결 해제하기
    dfs(core_index+1,precount,prelength)

def connect(x,y,d): # 해당 방향으로 전선을 연결하기
    while 0 < x < n-1 and 0 < y < n-1:
        x += dx[d]
        y += dy[d]
        arr[x][y] ^= 1

def check(x,y,d): # 해당 방향으로 나아갈 수 있는지 확인
    l = 0
    while 0 < x < n-1 and 0 < y < n-1:
        x += dx[d]
        y += dy[d]
        if arr[x][y] == 1:
            return 0
        l += 1
    return l


T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    # 방향 탐색
    dx = [1,0,0,-1]
    dy = [0,1,-1,0]

    # 코어 개수와 위치
    core = []
    core_count = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                core.append((i,j))
                core_count += 1

    answer = [0,0] # 개수, 길이
    dfs(0,0,0)
    print("#"+str(test_case),end=" ")
    print(answer[1])