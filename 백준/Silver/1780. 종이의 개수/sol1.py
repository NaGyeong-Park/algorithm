import sys

sys.stdin = open('input.txt')

sys.setrecursionlimit(10**7)
T = int(input())

def quad_tree(sx, sy, n):
    for i in range(sx,sx + n):
        for j in range(sy,sy+n):
            if map_lst[i][j] != map_lst[sx][sy]:
                n_size = n//3
                quad_tree(sx,sy, n_size)
                quad_tree(sx,sy+n_size,n_size)
                quad_tree(sx,sy+(2*n_size), n_size)

                quad_tree(sx+n_size, sy, n_size)
                quad_tree(sx+n_size, sy+n_size, n_size)
                quad_tree(sx+n_size, sy+(2*n_size),n_size)

                quad_tree(sx+(2*n_size), sy, n_size)
                quad_tree(sx+(2*n_size), sy+n_size,n_size)
                quad_tree(sx+(2*n_size), sy+(2*n_size), n_size)
                return
    cnt_dic[map_lst[sx][sy]] += 1
    return



for tc in range(1, T + 1):
    N = int(input())
    map_lst = [list(map(int, input().split())) for _ in range(N)]
    cnt_dic = {-1:0,0:0,1:0}
    quad_tree(0,0,N)
    for i in cnt_dic.values():
        print(i)