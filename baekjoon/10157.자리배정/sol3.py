import sys

sys.stdin = open('input.txt')

T = 3

def find_seat(C,R,num):
    move_lst = [R-1, C-1, R-1]
    seat = [C,1]
    cnt = (R-1)*2+C
    r_alpa = [0,1,0,-1]
    c_alpa = [-1,0,1,0]
    direc = [C-2, R-1]
    if num <= (R-1)*2+C:
        pass
    else:
        i = 0
        while True:
            if cnt>=num:
                break
            elif move_lst[-1] == 1:
                break
            else:
                move_lst.append(move_lst[-2] - 1)
                move_lst.append(move_lst[-2] - 1)
                seat[0] += move_lst[-2]*c_alpa[i]
                seat[1] += move_lst[-1]*r_alpa[i]
                cnt += move_lst[-2] + move_lst[-1]
                print(cnt)
                print(move_lst)
    return cnt



for tc in range(1, T + 1):
    C, R = map(int, input().split())
    num = int(input())
    a = find_seat(C,R,num)
    print(a)
    print('---')
