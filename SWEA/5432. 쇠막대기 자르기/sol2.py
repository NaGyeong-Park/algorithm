import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def find_laser(lst):
    cnt = 0
    l_cnt = 0
    sum = 0
    for i in range(len(lst)-1):
        if lst[i] == '(' and lst[i+1] != ')':
            for j in range(i+1,len(lst)):
                if lst[j] =='(' and lst[j+1] == ')':
                    cnt += 1
                elif lst[j] == ')' and lst[j-1] != '(':
                    if l_cnt == 0 :
                        sum += cnt+1
                        cnt = 0
                        break
                    else:
                        l_cnt -= 1
                elif lst[j] == '(':
                    l_cnt +=1
    return sum

for tc in range(1, T + 1):
    matrix = input()
    result = find_laser(matrix)
    print(f'#{tc} {result}')