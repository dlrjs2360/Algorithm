def solution(x,arr):
    status = int((n := len(arr)) % 2 != 0)
    arr2 = arr.copy()
    cnt = 0
    while 1:
        left, right = [], []
        for i in range(0, n, 2): left.append(arr2[i])
        for i in range(n - 1 - status, -1, -2): right.append(arr2[i])
        arr2 = left + right
        cnt += 1
        if arr.__eq__(arr2): break

    for k in range(x % cnt if cnt > 1 else 0):
        left, right = [], []
        for i in range(0, n, 2): left.append(arr[i])
        for i in range(n - 1 - status, -1, -2): right.append(arr[i])
        arr = left + right
    return "".join(arr)

print(solution(int(input()),list(input())))