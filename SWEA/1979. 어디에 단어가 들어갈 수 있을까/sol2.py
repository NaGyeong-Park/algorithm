import sys
import copy
sys.stdin = open('input.txt')

T = int(input())

# 찾는 수만큼 연속된 1을 찾기
def word_num_cnt(lst,num):
    #찾는 문자열
    find = '1'*num
    cnt = 0
    # lst안에서 find와 같은 문자열이 있다면 카운트
    for i in lst:
        for j in range(len(i)):
            if i[j] == find:
                cnt += 1
    return cnt

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    matrix2 = []
    for i in range(N):
        matrix2.append(list(input().split()))
    matrix1 = copy.deepcopy(matrix2)
    matrix2 = [x for x in zip(*matrix2)]
    for i in range(N):
        matrix1[i] = ''.join(matrix1[i]).split('0')
        matrix2[i] = ''.join(matrix2[i]).split('0')

    result = word_num_cnt(matrix1,K)
    result += word_num_cnt(matrix2,K)
    print(f'#{tc} {result}')