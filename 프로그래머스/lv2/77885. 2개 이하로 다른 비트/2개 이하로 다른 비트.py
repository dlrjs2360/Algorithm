'''
맨 오른쪽부터 탐색하면서 0을 만나면 1로 바꿔준다
만약 끝까지 갔는데 0을 못만났다면 10을 붙여서 [1:]와 더해준다.
'''

def convertor(bn):
    return sum([2**i for i in range(len(bn)) if bn[i] == '1'])

def f(num):
    num_bin = list(bin(num).split('b')[1])
    for i in range(len(num_bin:=num_bin[::-1])):
        if num_bin[i] == '0':
            num_bin[i] = '1'
            if i > 0:
                num_bin[i-1] = '0'
            break
    else:
        num_bin = num_bin[:-1]+['0','1'] 
    
    return convertor(num_bin)

def solution(numbers):
    return [f(num) for num in numbers]