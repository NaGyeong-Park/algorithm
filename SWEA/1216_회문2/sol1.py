import sys

sys.stdin = open('input.txt')

T = 10


# 행렬을 90도로 돌려주는 함수
def degree_change(matrix_small):
    num = len(matrix_small)
    change_matrix = []
    for i in range(num):
        change_matrix.append([])
    for j in range(num - 1, -1, -1):
        for i in range(num):
            change_matrix[i].append(matrix_small[j][i])
    return change_matrix


# 회문을 찾는 함수
def find_match(lst1, lst2):
    # 100개부터 시작해 글자수를 점점 줄여간다
    # num = 글자수 -1 : 인덱스에 넣기 위해 1을 빼줌
    num = 99
    result = 0
    # 회문을 찾을 때까지 돌아감
    while True:
        # 모든 행을 돈다
        for i in range(100):
            # 글자수만큼 행을 돈다
            # (ex) 글자수가 98이면 (0,98), (1,99)를 확인하기 때문에 2번
            for j in range(99 - num + 1):
                # 만약 글자와 반대글자가 같다면
                if lst1[i][j:num + j + 1] == lst1[i][num + j:j - 1:-1] or lst2[i][j:num + j + 1] == lst2[i][
                                                                                                    num + j:j - 1:-1]:
                    # 글자수를 return해준다.
                    result = num + 1
                    return result
        # if에 안걸리면 글자수를 1씩 줄이면서 다시 돌기
        num -= 1


for tc in range(1, T + 1):
    # 입력 받아줌
    tc_num = int(input())
    matrix1 = []
    for i in range(100):
        row = input()
        matrix1.append([])
        for j in range(100):
            matrix1[i].append(row[j])
    # 입력받은 matrix를 90도 돌려 세로줄 탐색을 쉽게 만들어준다.
    matrix2 = degree_change(matrix1)

    # 회문 찾는 함수 이용해 글자수를 도출해 출력해줌
    max = find_match(matrix1, matrix2)
    print(f'#{tc} {max}')