import sys

sys.stdin = open('input.txt')

T = 10


def calcul(n):
    # 인덱스 넘어가면
    if n >= N:
        return
    # 왼쪽의 가지가 있다면
    if tree[n][2] > 0:
        calcul(tree[n][2])
    # 오른쪽의 가지가 있다면
    if tree[n][3] > 0:
        calcul(tree[n][3])

    # 연산자라면 연산 후 결과값을 그 노드에 저장
    if tree[n][1] == '+':
        tree[n][1] = tree[tree[n][2]][1] + tree[tree[n][3]][1]
    elif tree[n][1] == '-':
        tree[n][1] = tree[tree[n][2]][1] - tree[tree[n][3]][1]
    elif tree[n][1] == '*':
        tree[n][1] = tree[tree[n][2]][1] * tree[tree[n][3]][1]
    elif tree[n][1] == '/':
        tree[n][1] = tree[tree[n][2]][1] / tree[tree[n][3]][1]


for tc in range(1, T + 1):
    N = int(input())
    tree = [[0] * 4 for _ in range(N + 1)]
    for i in range(N):
        lst = list(input().split())
        # 연산자라면
        if len(lst) == 4:
            tree[int(lst[0])][1] = lst[1]
            tree[int(lst[0])][2] = int(lst[2])
            tree[int(lst[0])][3] = int(lst[3])
        # 숫자라면
        else:
            tree[int(lst[0])][1] = int(lst[1])
    calcul(1)
    print(f'#{tc} {int(tree[1][1])}')