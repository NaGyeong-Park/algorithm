# 입력
map_size = list(map(int, input().split()))
point = list(map(int, input().split()))
hour = int(input())

# r값 c값 계산
r = (point[0]+hour)%(map_size[0]*2)
c = (point[1]+hour)%(map_size[1]*2)

# 만약 r값 c값이 범위를 벗어나면 map_size의 2배에서 그 r값, c값을 빼준다
if map_size[0]+1 <= r < map_size[0]*2:
    r = map_size[0]*2-r
if map_size[1]+1 <= c < map_size[1]*2:
    c = map_size[1]*2-c

#출력
print(r,c)