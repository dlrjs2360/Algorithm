def solution(e, starts):
    arr = [0]*(e+1)
    ans = [0]*(e+1)
    i = 2
    for i in range(2,e+1):
        for j in range(i,e+1,i):
            arr[j] += 1
    ans[e] = e
    for i in reversed(range(0,e)):
        if arr[i] >= arr[ans[i+1]]:
            ans[i] = i
        else:
            ans[i] = ans[i+1]
    return [ans[i] for i in starts]