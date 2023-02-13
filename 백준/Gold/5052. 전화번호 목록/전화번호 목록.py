T = int(input())
for test_case in range(T):
    n = int(input())
    arr = [input() for _ in range(n)]
    arr.sort()
    for i in range(n-1):
        if arr[i] == arr[i+1][:len(arr[i])]:
            print("NO")
            break
    else:
        print("YES")