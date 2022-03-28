def num(x,y):
    i = cnt = 0
    num = 1
    while True:
        map_lst[x][y] = num
        if num == K:
            return x,y
        next_x = x + direc_x[i]
        next_y = y + direc_y[i]
        if next_x < 0 or next_y < 0 or next_x >= R or next_y >= C or map_lst[next_x][next_y]:
            i += 1
            cnt += 1
            if cnt == 4:
                return 0
            if i == 4:
                i = 0
            x = x + direc_x[i]
            y = y + direc_y[i]
        else:
            x = next_x
            y = next_y
            cnt = 0
        num += 1

C, R = map(int,input().split())
K = int(input())
map_lst = [[0 for _ in range(C)] for _ in range(R)]
direc_x = [-1,0,1,0]
direc_y = [0,1,0,-1]
x = R-1
y = 0
result = num(x,y)
if not result:
    print(0)
else:
    print(result[1]+1,R-result[0])