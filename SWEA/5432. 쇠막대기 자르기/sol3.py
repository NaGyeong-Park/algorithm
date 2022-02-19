import sys

sys.stdin = open('sample_input.txt')

T = int(input())


def cut_stick(str):
    stick = 0
    sum = 0
    for i in range(len(str)):
        if str[i] == ')':
            if str[i-1] == '(':
                stick -= 1
                sum += stick
            else:
                sum += 1
                stick -= 1
        else:
            stick += 1
    return sum

for tc in range(1, T + 1):
    sticks = input()
    result = cut_stick(sticks)
    print(f'#{tc} {result}')