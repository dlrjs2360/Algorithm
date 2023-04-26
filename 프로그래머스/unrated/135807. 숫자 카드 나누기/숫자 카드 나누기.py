def solution(arrayA, arrayB):
    answer = 0
	
    # GCD a > b에 넣기 위해서 정렬
    arrayA.sort()
    arrayB.sort()
        
    gcd_A = arrayA[0]
    gcd_B = arrayB[0]
    
    # 각 배열들의 최대공약수
    for i in range(len(arrayA)):
        gcd_A = GCD(arrayA[i], gcd_A)

    for i in range(len(arrayB)):
        gcd_B = GCD(arrayB[i], gcd_B)
        
    if not isDiv(arrayA, gcd_B):
        answer = gcd_B
    if not isDiv(arrayB, gcd_A):
        answer = max(answer, gcd_A)
    return answer
 
# 최대공약수
def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)
 
# 나누어떨어지는지
def isDiv(array, gcd):
    for i in range(len(array)):
        if array[i] % gcd == 0:
            return True
    return False