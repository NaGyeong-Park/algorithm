import sys

sys.stdin = open('input.txt')

T = int(input())


def degree_change(matrix_small):
    num = len(matrix_small)
    change_matrix = []
    for i in range(num):
        change_matrix.append([])
    for j in range(num - 1, -1, -1):
        for i in range(num):
            change_matrix[i].append(matrix_small[j][i])
    return change_matrix


for tc in range(1, T + 1):
    print(f'#{tc} ')

    number = int(input())
    matrix = []
    for i in range(number):
        matrix.append(list(map(int, input().split())))

    A =  degree_change(matrix)
    B = degree_change(A)
    C = degree_change(B)
    result_lst = [A, B, C]

    for i in range(number):
        for k in range(3):
            for j in result_lst[k][i]:
                print(j,end='')
            print(end=' ')
        print()