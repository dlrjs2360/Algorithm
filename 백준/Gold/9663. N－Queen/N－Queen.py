def DFS(arr, row):
    global answer
    # 현재 열이 맨 끝까지 가면 종료
    if row >= n:
        answer += 1
        return
    # n개의 행을 모두 탐색
    for x in range(n):
        arr[row] = x  # 해당 열과 행에 퀸을 놓아보기 ( 열은 고정 )
        for y in range(row):  # 지금까지 놓은 퀸들과 비교해서 조건을 만족하면 다음 탐색 이어가기
            if arr[y] == arr[row] or abs(row - y) == abs(arr[row] - arr[y]):
                break
        else:
            DFS(arr, row+1)


n = int(input())
answer = 0

queen = [0] * n
DFS(queen, 0)

print(answer)