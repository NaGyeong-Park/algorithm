import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def change_lst(lst):
    i = 0
    l_num = 0
    while i < len(lst)-1:
        if lst[i] == '(' and lst[i+1] == ')':
            lst[i:i+2] = ['*']
        elif lst[i] == '(':
            l_num += 1
            lst[i] = l_num
        else:
            lst[i] = l_num
            l_num -= 1
        i += 1
    lst[i] = 1
    return lst

def make_idx_lst(lst):
    idx_lst = []
    for i in range(len(lst)):
        idx_lst.append(i)
    return idx_lst

def find_laser(lst,idx_lst):
    i = 0
    j = 0
    cnt = 0
    stick = 0
    for i in idx_lst:
        if i == 'X' or lst[i]=='*':
            pass
        else:
            j = i + 1
            while True:
                if lst[j] == lst[i]:
                    idx_lst[j] = 'X'
                    stick += cnt+1
                    cnt = 0
                    break
                elif lst[j] == '*':
                    cnt += 1
                j += 1
    return stick



for tc in range(1, T + 1):
    matrix_str = input()
    matrix = []
    for i in range(len(matrix_str)):
        matrix.append(matrix_str[i])
    new_matric = change_lst(matrix)
    idx_lst = make_idx_lst(new_matric)
    result = find_laser(new_matric,idx_lst)

    print(f'#{tc} {result}')

