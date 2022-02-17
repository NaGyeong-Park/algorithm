import sys

sys.stdin = open('sample_input.txt')

T = int(input())

# 입력받은 리스트들 중 요소 길이가 가장 긴 값 찾기
def find_max_len(lst):
    max = len(lst[0])
    for i in range(5):
        if max < len(lst[i]):
            max = len(lst[i])
    return max

# 만약 리스트의 요소 중 가장 긴 요소보다 길이가 짧다면
# *을 추가해 길이를 가장 큰 것으로 맞춰줌
def change_lst(lst,max_num):
    for i in range(5):
        if len(lst[i]) != max_num:
            n = max_num-len(lst[i])
            for j in range(n):
                lst[i].append('*')
    return lst

for tc in range(1, T + 1):
    lst = []
    # 입력받기
    for i in range(5):
        lst.append([])
        row = input()
        for j in range(len(row)):
            lst[i].append(row[j])
        row = []

    # 함수 수행
    max = find_max_len(lst)
    new_lst = change_lst(lst,max)

    # 프린트
    print(f'#{tc} ',end='')
    for i in range(max):
        for j in range(5):
            if lst[j][i] == '*':
                continue
            else:
                print(lst[j][i], end='')
    print()

