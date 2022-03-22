import sys

sys.stdin = open('input.txt')

sys.setrecursionlimit(10**7)
T = int(input())

def quad_tree(sx, sy, ex,ey):
    global result
    cheak = 1
    for i in range(sx,ex):
        for j in range(sy,ey):
            if map_lst[i][j] != map_lst[sx][sy]:
                cheak = 0
                break
    if cheak == 1:
        print(map_lst[sx][sy], end = '')
        return
    print('(', end = '')
    quad_tree(sx,sy,(sx+ex)//2,(sy+ey)//2)
    quad_tree(sx,(sy+ey)//2,(sx+ex)//2,ey)
    quad_tree((sx+ex)//2, sy, ex, (sy+ey)//2)
    quad_tree((sx+ex)//2,(sy+ey)//2,ex,ey)
    print(')', end='')


for tc in range(1, T + 1):
    N = int(input())
    map_lst = [list(map(int, input())) for _ in range(N)]
    result = [1]
    quad_tree(0,0,N,N)
    print()