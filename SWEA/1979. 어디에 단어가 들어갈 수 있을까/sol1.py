import sys
import copy
sys.stdin = open('input.txt')

T = int(input())

# 찾는 수만큼 연속된 1을 찾기
def word_num_cnt(lst,num):
    # 찾는 문자열
    find = '1'*num
    cnt = 0
    # lst안에서 find와 같은 문자열이 있다면 카운트
    for i in lst:
        for j in range(len(i)):
            if i[j] == find:
                cnt += 1

    return cnt

# 전치행렬 만들기
def transpose(lst):
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if i < j:
                lst[i][j], lst[j][i] = lst[j][i], lst[i][j]
    return lst


for tc in range(1, T + 1):
    # N, k 입력
    N, K = map(int, input().split())
    matrix2 = []
    # matrix 입력
    for i in range(N):
        matrix2.append(list(input().split()))
    # 처음 matrix deepcopy로 저장
    matrix1 = copy.deepcopy(matrix2)
    # 처음 matrix의 전치행렬 만들어주기 : 세로줄도 탐색하기 위해서
    matrix2 = transpose(matrix2)
    print(matrix1)
    # 리스트의 열 요소들을 합쳐 문자열로 바꿔주기 : ex) ['1','0','0'] => '100' : ''.join(lst)
    # 변환된 문자열을 0을 기준으로 나누기 : ex) '100' => ['1','',''] : .split('0')
    for i in range(N):
        matrix1[i] = ''.join(matrix1[i]).split('0')
        matrix2[i] = ''.join(matrix2[i]).split('0')

    # 찾는 수만큼 연속된 1을 찾아 카운트 한 값들을 결과로 내보내기
    result = word_num_cnt(matrix1,K)
    result += word_num_cnt(matrix2,K)
    print(f'#{tc} {result}')