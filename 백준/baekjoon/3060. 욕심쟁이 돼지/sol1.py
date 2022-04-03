import sys

sys.stdin = open('input.txt')

T = int(input())

def find_day(N, lst):
    new_lst = [0]*6
    lst_sum = cnt = 0
    while lst_sum < food:
        cnt += 1
        for i in range(6):
            idx_lst = [i+1,i-1,i+3,i]
            for idx in range(4):
                if idx_lst[idx] >= 6:
                    idx_lst[idx] = idx_lst[idx] - 6
                elif idx_lst[idx] < 0:
                    idx_lst[idx] = idx_lst[idx] + 6
                new_lst[i] += lst[idx_lst[idx]]
        lst_sum = sum(lst)
        if lst_sum > N:
            return cnt
        lst_sum = 0
        lst = new_lst
        new_lst = [0] * 6

for tc in range(1, T + 1):
    food = int(input())
    pig_quantity = list(map(int, input().split()))
    print(find_day(food, pig_quantity))