import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    
    print(f'#{tc} ', end='')
    n = int(input())                # 정수를 입력받는다
    n = (n**(1/3))                  # 세제곱근
    n = str(n)                      # 인덱스 활용을 위해 문자열로 바꿔줌
    dot = n.index('.')              # 소수점 . 인덱스를 찾아 소수점들 숫자로 판단

    if n[dot+1] == '0' and len(n) == dot+2 :    # . 뒤에 0이고, 문자열이 0에서 끝난다면(인덱스이기에 dot+1+1)
        print(int(n[0:dot]))        # . 앞자리만 출력
    elif n[dot+1] == '9' and n[dot+2] == '9':   # . 뒤에 99라면
        print(int(n[0:dot])+1)      # . 앞자리에 1을 더해 출력
    else:
        print(-1)                   # 윗 케이스에 해당하지않으면 -1 출력