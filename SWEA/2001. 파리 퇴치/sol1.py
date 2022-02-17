import sys

sys.stdin = open('input.txt')

T = int(input())

def find_best_killer(lst,num):
    sum = 0
    max = 0
    turn_num = len(lst)-num+1+1
    for _ in range(num*num):
        for r in range(num):
            for c in range(num):

                sum = lst[r][c:c+num]
                sum2 = lst[r+num][c:c+num]
                print(sum)
            print('--')



for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = []
    for i in range(N):
        matrix.append([])
        row = list(map(int,input().split()))
        for j in row:
            matrix[i].append(j)
    print(matrix)
    find_best_killer(matrix,M)

    print(matrix)
    print(f'#{tc} ')

