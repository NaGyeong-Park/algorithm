N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# A, B를 오름차순으로 정렬해줌
A.sort()
B.sort()
result = 0
a_max_index = b_max_index = N-1

# 큰 수부터 차례대로 내려가 N번 탐색
for i in range(N, 0, -1):
    # 아직 B로 바꿀 횟수가 남아있다면
    if K > 0:
        # B의 큰 수가 A의 큰 수보다 크다면 바꾸는 횟수 차감, 결과 값에 B의 큰 수를 더하고 한 인덱스 내려감
        if B[b_max_index] > A[a_max_index]:
            result += B[b_max_index]
            b_max_index -= 1
            K -= 1
        # 아니라면 결과값에 A의 큰 수를 더하고 한 인덱스 내려감
        else:
            result += A[a_max_index]
            a_max_index -= 1
    # 바꿀 횟수가 없다면 A를 차례대로 더하고 끝
    else:
        result += A[a_max_index]
        a_max_index -= 1

print(result)