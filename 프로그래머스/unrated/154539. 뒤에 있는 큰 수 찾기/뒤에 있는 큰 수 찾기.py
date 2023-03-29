def solution(numbers):
    answer = [-1] * len(numbers)
    backMax = numbers[-1]
    for i in range(len(numbers)-2,-1,-1):
        if numbers[i] >= backMax:
            backMax = numbers[i]
            continue
        for j in range(i+1,len(numbers)):
            if numbers[j] > numbers[i]:
                answer[i] = numbers[j]
                break    
            if numbers[i] >= numbers[j] and numbers[i] < answer[j]:
                answer[i] = answer[j]
                break
                
            
    return answer