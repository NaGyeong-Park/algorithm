N = int(input())
direction =  {"L":[0, -1], "R":[0, 1], "U":[-1, 0], "D":  [1, 0]}
result = [1,1]
data = input().split()
for dir in data:
    now_x, now_y = direction[dir]
    if (result[0] + now_x < 1) or (result[1] + now_y < 1):
        pass
    else:
        result[0] += now_x
        result[1] += now_y
print(result)