import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    map_size = list(map(int, input().split()))
    point = list(map(int, input().split()))
    hour = int(input())

    r = (point[0] + hour) % (map_size[0] * 2)
    c = (point[1] + hour) % (map_size[1] * 2)

    if map_size[0] + 1 <= r < map_size[0] * 2:
        r = map_size[0] * 2 - r
    if map_size[1] + 1 <= c < map_size[1] * 2:
        c = map_size[1] * 2 - c
    print(r, c)