import sys
from itertools import permutations
sys.stdin = open('input.txt')

T = int(input())

# triplet과 run을 검사하는 babygin 검사 함수
def trirun(lst_slice):
    # triplet
    if lst_slice[0] == lst_slice[1] == lst_slice[2]:
        return 1
    # run
    elif lst_slice[0] == lst_slice[1]-1 and lst_slice[1] == lst_slice[2]-1:
        return 1
    return 0

# 둘 다 카드 6장을 받았을 때 babygin 확인하는 함수
def cheak(lst):
    max = 0
    for i in lst:
        a = trirun(i[:3])
        b = trirun(i[3:])
        if a+b == 2:
            return 2
        if max < a+b:
            max = a+b
    return max

# 카드를 아직 다 받지 못했을 때(3~5장) babygin 확인하는 함수
def cheak_early(lst):
    for k in lst:
        a = trirun(k)
        if a == 1:
            return 1
    return 0


for tc in range(1, T + 1):
    print(f'#{tc} ',end='')
    lst = list(map(int, input().split()))
    lst1 = lst[::2]
    lst2 = lst[1::2]
    vaild = 0                                           # 카드 다 뽑기 전에 누가 이겼는지 체크하는 변수
    for i in range(3,6):                                # 카드를 다 뽑기 전에
        lst1_early = list(permutations(lst1[:i],3))     # 3개로 이루어진 순열을 뽑아내기
        lst2_early = list(permutations(lst2[:i],3))
        early1 = cheak_early(lst1_early)                # babygin 확인 함수 돌리기
        early2 = cheak_early(lst2_early)
        if early1 == early2 == 1 or early1 > early2:    # 둘 중 1명이라도 1이 나오면 게임이 끝난거임
            print(1)
            vaild = 1
            break
        elif early2 > early1:
            print(2)
            vaild = 1
            break
    if vaild == 1:
        continue
    else:                                               # 카드 다 뽑을 때까지 아무도 못이겼다면
        lst1 = list(permutations(lst1))                 # 6개로 이루어진 순열 뽑아내기
        lst2 = list(permutations(lst2))
        result1 = cheak(lst1)                           # babygin 확인 함수 돌리기
        result2 = cheak(lst2)
        if result1 == result2 == 0:                     # 둘다 0이라면 무승부
            print(0)
        elif result1 < result2:                         # 2가 더 큰 경우만 2가 이김(첫 번째가 먼저 뽑응께)
            print(2)
        else:
            print(1)

