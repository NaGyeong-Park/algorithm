import sys

sys.stdin = open('input.txt')

T = int(input())

def Factorization(num):
    dic_num = {2:0, 3:0, 5:0, 7:0, 11:0}
    dic_keys = list(dic_num.keys())
    i = 0
    while True:
        if i == 5:
            break
        if num % dic_keys[i] != 0:
            print(f' {dic_num[dic_keys[i]]}', end='')
            i += 1
        else:
            num = num//dic_keys[i]
            dic_num[dic_keys[i]] += 1
    return print()

for tc in range(1, T + 1):
    num = int(input())
    print(f'#{tc}', end='')
    result = Factorization(num)

