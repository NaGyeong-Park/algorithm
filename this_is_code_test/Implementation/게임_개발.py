N, M = map(int, input().split())
now_x, now_y, now_direc = map(int, input().split())
d = [(-1,0), (0,1), (1,0), (0,-1)]
data=[]
result = 1
for i in range(N):
    data.append(list(map(int, input().split())))
    if i == now_x:
        data[now_x][now_y] = True

while True:
    block = 0
    for i in range(4):
        temp_x = now_x+d[now_direc][0]
        temp_y = now_y+d[now_direc][1]
        if data[temp_x][temp_y] == 1 or data[temp_x][temp_y] == True:
            block += 1
            now_direc = (now_direc+1)%4
        else: 
            now_x = temp_x
            now_y = temp_y
            data[now_x][now_y] = True
            result +=1
            break
    if block == 4:
        if data[temp_x][temp_y] == 0:
            now_x = temp_x
            now_y = temp_y
        else:
            break
print(result)