import sys

sys.stdin = open('input.txt')

T = int(input())

def is_it_wrong(lst):
    cheak_dic = {}
    for i in range(1,10):
        cheak_dic[i] = 0
    A = find_row_col(lst,cheak_dic)
    B = find_box(lst,cheak_dic)
    if A+B == 2:
        return 1
    else:
        return 0

def find_row_col(lst,cheak_dic):
    for i in range(9):
        for j in range(9):
            cheak_dic[lst[i][j]] += 1
            cheak_dic[lst[j][i]] += 1
        for k in range(1,10):
            if cheak_dic[k] != 2:
                return 0
            else:
                cheak_dic[k] = 0
    return 1

def find_box(lst,cheak_dic):
    for i in range(0,9,3):
        for j in range(0,9,3):
            for ii in range(i, i+3):
                for jj in range(j,j+3):
                    cheak_dic[lst[ii][jj]] += 1
            for k in range(1,10):
                if cheak_dic[k] != 1:
                    return 0
                else:
                    cheak_dic[k] = 0
    return 1


for tc in range(1, T + 1):

    matrix = [list(map(int,input().split())) for _ in range(9)]

    print(f'#{tc} {is_it_wrong(matrix)}')

