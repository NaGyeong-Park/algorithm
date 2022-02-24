import sys

sys.stdin = open('input.txt')

T = 10


# 후위 표기법 변환 함수
def trans(str):
    stack = []                              # 스택 생성
    result = []                             # return 리스트

    for coin in str:
        if coin.isdigit():                  # 요소가 숫자라면
            result.append(coin)             # 결과 리스트에 넣어주기
        else:
            if not stack:                   # 스택이 비어있다면
                stack.append(coin)          # 연산자 stack에 넣어주기
            else:                           # 안비어있으면 : 우선순위 : ( > *,/ > +,-
                if coin == "(":             # 우선순위 별로 조건 다르게 해서 넣어주기
                    stack.append(coin)      # 최 우선순위는 그냥 넣어주기
                elif coin == ")":           # )가 들어가면
                    pop_att = stack.pop()   # stack에서 (이 나올때까지 다 꺼내버리기
                    while pop_att != "(":
                        result.append(pop_att)
                        pop_att = stack.pop()
                elif coin == "*" or coin == "/":    # 만약 *나 /면
                    while stack and (stack[-1] == "*" or stack[-1] == "/"):
                        result.append(stack.pop())  # 스택 마지막에 있는게 *나 /가 아니면
                    stack.append(coin)              # stack에 그대로 쌓기
                elif coin == "+" or coin == "-":    #  +나 / 면
                    while stack and stack[-1] != "(": # 닫는 괄호가 나오기 전까지 pop
                        result.append(stack.pop())
                    stack.append(coin)                # +나 - 스택에 넣어주기

    # 스택에 뭐가 있으면 결과 리스트에 다 넣어주기
    for coin in range(len(stack)):
        result.append(stack.pop())
    return result

# 후위표기법 계산기
def postfix_notation(str):
    stack = []                          # 스택 생성
    for coin in str:                    # 리스트 길이만큼 반복
        if coin.isdecimal():            # 리스트 요소가 숫자면 stack에 정수형태로 넣어주기
            stack.append(int(coin))
        elif len(stack) >= 2:           # 스택에 남은 요소가 2개 이상이면
            if coin == '+':             # 사칙연산이 들어오면 top에서 두개 꺼내 계산해서 다시 스택에 넣어주기
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a+b))
            elif coin == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a-b))
            elif coin == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a*b))
            elif coin == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))
        elif coin == '.':               # '.'은 마지막, 스택에 남은 요소가 1개일 때만 스택값 return
            if len(stack) == 1:
                return int(stack.pop())
            else:
                return 'error'
        else:                           # 이외의 경우는 있을 수 없으므로 error return
            return 'error'
    if len(stack) != 1:                 # for문을 다 돌고 나왔는데 stack에 여러 요소가 남아있으면 error
        return 'error'                  # ex) 숫자가 많고, 연산자가 적을 때
    return stack[0]




for tc in range(1, T + 1):
    leng = int(input())
    str = input()
    a = trans(str)
    print(f'#{tc} {postfix_notation(a)}')

