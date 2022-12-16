NOW = input()

direction = [[-2,1],[-2,-1],[2,1],[2,-1],[1,-2],[1,2],[-1,-2],[-1,2]]
x_num = {"a":1, "b":2,"c":3, "d":4, "e":5,"f":6,"g":7,"h":8}
now_x = x_num[NOW[0]]
now_y = int(NOW[1])
result= 8
for direc in direction:
    move_x = now_x + direc[0]
    move_y = now_y + direc[1]
    if move_x < 1 or move_y < 1 or move_x > 8 or move_y > 8:
        result -= 1
print(result)