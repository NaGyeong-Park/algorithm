import sys

sys.stdin = open('input.txt')

T = int(input())

# max값 찾는 함수
def max_num_sum(args):
# 리스트의 최대값 기준 및 합산 초기화
    max_number = args[0]
    max_sum = 0
# 기준점이 0 index라서 1부터 시작
# 기준점에서 다음 인덱스보다 크면 차이만큼 더하고 작거나 같으면 새로운 기준점 할당
    for i in range(1, n):
        if max_number > args[i]:
            max_sum += max_number - args[i]
        else:
            max_number = args[i]
    return max_sum

# 테스트 케이스 입력
for tc in range(1, T + 1):
    n = int(input())
# 입력 받은 리스트를 슬라이싱 해서 뒤집기
    numbers = list(map(int, input().split()))[::-1]

# 함수 호출
    rlt = max_num_sum(numbers)

# 출력
    print(f'#{tc} {rlt}')