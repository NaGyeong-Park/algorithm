import sys

sys.stdin = open('input.txt')

from itertools import combinations

T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split()) # 사람수, 선반 높이
    h_lst = list(map(int, input().split())) # 직원들 키
    com_lst = [] # 부분집합 모음 리스트 만들기
    result = sum(h_lst) # 결과값 초기화
    for i in range(len(h_lst)+1):   # combinations 함수를 이용해 모든 부분집합 구하기
        com_lst += list(combinations(h_lst,i))
    for j in range(len(com_lst)):   # 모든 부분집합을 돌아다니며 합을 구함
        sum_num = sum(com_lst[j])   
        if sum_num >= B and sum_num < result: # 결과값보다 크고, 기존 resul 값보다 작다면
            result = sum_num    # 결과값 바꿔주기

    print(f'#{tc} {result-B}')