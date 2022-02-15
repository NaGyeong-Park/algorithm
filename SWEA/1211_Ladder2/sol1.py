import sys

sys.stdin = open('input4.txt')

T = 10

# 사다리타기
def find_idx(ladder,start_num):
    # 거꾸로 올라가기 위해 행은 99
    row = 99
    num = 0
    # 행이 1일때 까지 반복
    while row > 0:
        # 열을 세 개로 분리해준 이유 : 인덱스 에러를 막기 위해
        # 만약 열이 0과 99 사이라면
        if 1 < start_num < 98:
            # 양 옆을 확인해 1이 있는 쪽으로 열을 옮겨준다.
            if ladder[row][start_num + 1] == 1:
                while ladder[row][start_num+1] == 1 and start_num != 98:
                    start_num += 1
                    num += 1
                    # 만약 열이 98이고 99열의 값이 1이라면 열을 99로 만들고 while문을 나옴
                    # 인덱스 에러를 막기 위함
                    if start_num == 98 and ladder[row][start_num+1] == 1:
                        start_num +=1
                        num += 1
                        break
            elif ladder[row][start_num - 1] == 1:
                while ladder[row][start_num-1] == 1 and start_num !=1:
                    start_num -= 1
                    num +=1
                    # 만약 열이 1이고 0열의 값이 1이라면 열을 0로 만들고 while문을 나옴
                    # 인덱스 에러를 막기 위함
                    if start_num == 1 and ladder[row][start_num-1] == 1:
                        start_num -=1
                        num +=1
                        break
        # 만약 열이 0이라면 오른쪽 열들만 확인해줌
        elif start_num == 0:
            if ladder[row][start_num+1] == 1:
                while ladder[row][start_num+1] == 1:
                    start_num += 1
                    num += 1
        # 만약 열이 99이라면 오른쪽 열들만 확인해줌
        elif start_num == 99:
            if ladder[row][start_num-1] == 1:
                while ladder[row][start_num-1] == 1:
                    start_num -= 1
                    num += 1
        row -=1
    return num, start_num



for tc in range(1, T + 1):
    # 입력에 변수 할당 처리
    num = int(input())
    ladder = []
    for i in range(100):
        arr = list(map(int, input().split()))
        ladder.append(arr)

    # 마지막 줄에서 정답이 되는 '2'의 인덱스를 찾는다
    line_idx = []
    for i in range(100):
        if ladder[99][i] == 1:
            line_idx.append(i)

    # 함수 이용
    result = []
    for i in line_idx:
        result.append(find_idx(ladder, i))

    min = result[0][0]
    min_idx = result[0][1]
    for i in range(len(result)):
        if result[i][0] < min:
            min = result[i][0]
            min_idx = result[i][1]
    # 출력
    print(f'#{tc} {min_idx}')
