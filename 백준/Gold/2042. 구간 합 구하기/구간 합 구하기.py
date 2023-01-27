
# 세그먼트 트리 초기화
# start, end: 범위(구간), node: 세그먼트 트리에서 노드 번호
def init(start, end, node):
    # start와 end가 같다는 것은 leaf node임을 의미한다.
    if start == end:
        tree[node] = nums[start]
        return

    mid = (start + end) // 2
    init(start, mid, node * 2)  # 왼쪽 자식 노드의 구간합
    init(mid + 1, end, node * 2 + 1)  # 오른쪽 자식 노드의 구간합

    # 왼쪽 자식 노드에 있는 구간합과 오른쪽 자식 노드에 있는 구간합을 더한 값을 저장
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


# 세그먼트 트리의 구간합
# L: 구하고자 하는 구간합의 왼쪽 구간
# R: 구하고자 하는 구간합의 오른쪽 구간
# node: 현재 노드
# nodeLeft: 노드의 왼쪽 구간
# nodeRight: 노드의 오른쪽 구간
def sum(L, R, node, nodeLeft, nodeRight):
    # 구하고자 하는 구간합의 구간 안에 현재 노드의 구간이 포함되지 않는다면
    # 0을 반환한다.
    if R < nodeLeft or nodeRight < L:
        return 0

    # 구하고자 하는 구간합의 구간 안에 현재 노드의 구간이 포함된다면
    # 현재 노드의 값을 반환한다.
    if L <= nodeLeft and nodeRight <= R:
        return tree[node]

    # 구간이 겹치는 경우에는 자식 노드에 대하여 sum 함수를 호출한다.
    mid = (nodeLeft + nodeRight) // 2
    return sum(L, R, node * 2, nodeLeft, mid) + sum(L, R, node * 2 + 1, mid + 1, nodeRight)


# 세그먼트 트리 업데이트
# L: 노드의 왼쪽 구간
# R: 노드의 오른쪽 구간
# node: 현재 노드
# idx: 바꿀 값의 인덱스
# val: 바꿀 값
def update(L, R, node, idx, val):
    if L == R == idx:  # 단일 구간 업데이트
        tree[node] = val
        return

    # 현재 노드의 구간에 idx가 포함되지 않을 경우
    # 작업 없이 종료
    if idx < L or R < idx:
        return

    mid = (L + R) // 2
    update(L, mid, node * 2, idx, val)  # 왼쪽 자식 노드 업데이트
    update(mid + 1, R, node * 2 + 1, idx, val)  # 오른쪽 자식 노드 업데이트
    tree[node] = tree[node * 2] + tree[node * 2 + 1]  # 업데이트된 자식 노드들을 더해서 현재 노드의 값에 저장


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    nums = []
    tree = [0 for _ in range(N * 4)]

    for _ in range(N):
        nums.append(int(input()))

    init(0, N - 1, 1)

    for _ in range(M + K):
        a, b, c = map(int, input().split())

        if a == 1:
            b -= 1
            update(0, N - 1, 1, b, c)
        else:
            b -= 1
            c -= 1
            print(sum(b, c, 1, 0, N - 1))
