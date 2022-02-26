# 초기 아이디어 제출 코드
# 런타임 에러

map_size = list(map(int,input().split()))
point = list(map(int,input().split()))
hour = int(input())

r_move = 1
c_move = 1

for i in range(hour):
    if point[0] == 0 or point[0] == map_size[0]:
        r_move = -r_move
    if point[1] == 0 or point[1] == map_size[1]:
        c_move = -c_move
    point[0] += r_move
    point[1] += c_move

print(point[0],point[1])