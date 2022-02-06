number = int(input())
matrix_lst = []
for i in range(number):
    matrix_size = int(input())
    matrix_lst.insert(i,[])

    for j in range(matrix_size):
        matrix = list(map(int, input().split()))
        matrix_lst[i].append(matrix)


def degree_change(matrix_small):
    num = len(matrix_small)
    change_matrix = []
    for i in range(num):
        change_matrix.append([])
    for j in range(num-1, -1, -1):
        for i in range(num):
            change_matrix[i].append(matrix_small[j][i])
    return change_matrix

for i in range(number):
    gijoon = len(matrix_lst[i][0])
    change_lst = []
    change_lst.append(degree_change(matrix_lst[i]))
    change_lst.append(degree_change(change_lst[1]))
    change_lst.append(degree_change(change_lst[2]))
    print(f'#{i+1}')
    for index in range(gijoon):
        for i in range(3):
            for j in range(gijoon):
                print(change_lst[i][index][j], end='')
            print(end=' ')
        print()