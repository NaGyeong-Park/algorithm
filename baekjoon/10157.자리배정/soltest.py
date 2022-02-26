T = int(input())

def find_seat(lst, num,N,M):
    r_idx = [0,1,0,-1]
    c_idx = [1,0,-1,0]
    cnt = r = c = 1
    i = 0

    while 1<=r<N+1 and 1<=c<M+1:
        if cnt == num:
            break
        lst[r][c] = cnt
        cnt += 1
        if r+r_idx[i] == N+1 or c+c_idx[i] == M+1 or lst[r+r_idx[i]][c+c_idx[i]]:
            i = (i+1)%4
        r = r_idx[i] + r
        c = c_idx[i] + c
    return r,c


for tc in range(1, T + 1):
    N, M = map(int,input().split())
    num = int(input())
    if num > N*M:
        print(0)
    else:
        matrix = [['*'] * (N + 2)]
        [matrix.append([0] * (N + 2)) for _ in range(M)]
        matrix += [['*'] * (N + 2)]
        for i in range(1, N+1):
            matrix[i][0] = matrix[i][-1] = '*'
        result = find_seat(matrix,num,N,M)
        print(result[0],result[1])