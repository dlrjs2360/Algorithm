def post_order(x):
    if x:
        post_order(left[x])
        post_order(right[x])

        if tree[x] == "+":
            tree[x] = int(tree[left[x]]) + int(tree[right[x]])
        elif tree[x] == "-":
            tree[x] = int(tree[left[x]]) - int(tree[right[x]])
        elif tree[x] == "*":
            tree[x] = int(tree[left[x]]) * int(tree[right[x]])
        elif tree[x] == "/":
            tree[x] = int(tree[left[x]]) // int(tree[right[x]])

for test_case in range(1,11):
    n = int(input())
    tree, left, right = [0] * (n+1), [0] * (n+1), [0] * (n+1)
    for _ in range(n):
        arr = input().split()
        tree[int(arr[0])] = arr[1]
        if len(arr) == 4:
            left[int(arr[0])] = int(arr[2])
            right[int(arr[0])] = int(arr[3])

    post_order(1)
    print(f'#{test_case} {tree[1]}')