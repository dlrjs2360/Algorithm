arr = list(input())

st = []
temp = 1
result = 0


for i in range(len(arr)):
    
    if arr[i] == '(':
        st.append(arr[i])
        temp *= 2
        
    
    elif arr[i] == '[':
        st.append(arr[i])
        temp *= 3
        
    
    elif arr[i] == ')':
        if not st or st[-1] == '[':
            result = 0
            break
        if arr[i-1] == '(':
            result += temp
        st.pop()
        temp //= 2
        
    else :
        if not st or st[-1] == '(':
            result = 0
            break
        if arr[i-1] == '[':
            result += temp
        st.pop()
        temp //= 3
        
if st:
    print(0)
else:   
    print(result)