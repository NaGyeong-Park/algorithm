import sys

sys.stdin = open('s_input.txt')

T = int(input())




for tc in range(1, T + 1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    lst = []
    # Ai X Aj 리스트 생성
    for i in range(N):
        for j in range(i+1,N):
            # 모든 짝을 곱하되, 한자리 수는 리스트에 넣지 않는다
            num = num_lst[i]*num_lst[j]
            if num//10 != 0:
                lst.append(num)
    lst.sort(,,-1)
    print(lst)
    # 단조 증가하는 수 중 max값 찾는 함수 이용해 결과 도출
    max = -1
    # Ai*Aj 모든 수 만큼 for문 돌림
    for i in range(len(lst)):
        # 10으로 나눠준 나머지 값의 초기값을 9로 설정
        last_num = 9
        num = lst[i]

        while True:
            # 만약 num이 1의 자리가 되었을 때
            if num//10 == 0:
                # 이전숫자 값보다 작다면
                if num%10 <= last_num:
                    # max값보다 원래 수의 크기가 크다면
                    if lst[i] > max:
                        # max값을 바꿔줌
                        max = lst[i]
                break
            # num을 10으로 나눈 나머지가 전 숫자보다 작다면
            # last_num을 현재 num을 10으로 나눠준 나머지 값으로 바꿔주고
            # num값 자체를 10으로 나눈 몫을 넣어줌
            elif num%10 <= last_num:
                last_num = num%10
                num = num//10
            # 위 두 경우 포함되지 않으면 단조 증가하는 수가 아니므로 break
            else:
                break

    print(f'#{tc} {max}')
