import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    #상자의 갯수 N, 바꾸는 횟수 Q 입력 받기
    N, Q = map(int, input().split())
    #N개의 길이의 0이 요소인 리스트를 만들어줌
    N_lst = [0]*N

    #바꾸는 횟수만큼 for문을 돌린다
    for i in range(Q):
        #바꾸는 범위 A,B를 입력받음
        A, B = map(int, input().split())
        #N_lst를 A~B만큼 슬라이싱해 요소들을 현재 인덱스값+1(상자번호가 1부터 시작)으로 바꿔줌
        N_lst[A-1:B] = [i+1]*(B-A+1)
    #출력
    print(f'#{tc}', end='')
    for i in N_lst:
        print(f' {i}', end='')
    print()