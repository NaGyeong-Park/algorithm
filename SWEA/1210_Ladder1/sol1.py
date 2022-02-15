import sys

sys.stdin = open('open.txt')

T = 1

def play(line, ladder):
    col = 0
    while col < 99:
        if line+1 != 100 or line-1 != -1:
            if ladder[col][line+1] == 1:
                while ladder[col][line+1] == 1 and line+1 < 100:
                    line += 1
                print(f'cold: {col}')
                print(f'line: {line}')
                col += 1
            if ladder[col][line-1] == 1:
                while ladder[col][line-1] == 1 and line-1 > -1:
                    line -= 1
                col += 1
            if ladder[col][line] == 1:
                if col != 99:
                    col += 1
        print(line)
    print(f'{line}line')
    print(f'{col}col')
    return ladder[line][col], line

for tc in range(1, T + 1):

    num = int(input())
    ladder = []
    for i in range(100):
        arr = list(map(int, input().split()))
        ladder.append(arr)
    line_idx = []

    for i in range(100):
        if ladder[0][i] == 1 :
            line_idx.append(i)

# for elem in line_idx:
    result = play(67,ladder)
    print('---')
    print(result)
    if result[0] == 2:
        print(result[1])
        break

    print(f'#{tc} ')

