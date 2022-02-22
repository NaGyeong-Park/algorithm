import sys

sys.stdin = open('sample_input.txt')

# 테스트 케이스 갯수
T = int(input())

for tc in range(1, T + 1):
    # 이동하는 학생 수
    N = int(input())
    check_list = [0] * 201 # 복도 리스트 : 홀수 짝수 신경쓰지 않기위해 201개 만들어줌
    for _ in range(N):     # ex) 1~2번 방 이동 : 인덱스 1 / 3~4번방 : 인덱스 2
        a, b = map(int, input().split())
        if a > b : a, b = b, a # 앞자리 수가 더 크면 순서 바꿈
        a = (a + 1) // 2
        b = (b + 1) // 2
        for i in range(a, b+1): # a~b까지 돌아간 복도에 1을 더해줌
            check_list[i] += 1
    print(f'#{tc} {max(check_list)}') # 제일 큰 값 출력