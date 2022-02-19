import sys

sys.stdin = open('input.txt')

T = int(input())

def find_best_killer(lst,M,N):
    sum = 0
    max = 0
    repeat_num = N - M + 1
    for i in range(repeat_num):
        for j in range(repeat_num):
            sum = 0
            for ii in range(i,M+i):
                for jj in range(j,j+M):
                    sum += lst[ii][jj]
            if max < sum:
                max = sum
    return max

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = []
    for i in range(N):
        matrix.append([])
        row = list(map(int,input().split()))
        for j in row:
            matrix[i].append(j)
    result = find_best_killer(matrix,M,N)
    print(f'#{tc} {result}')

