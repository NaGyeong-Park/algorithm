import sys

sys.stdin = open('input.txt')

T = 10

# 후위 표기법 변환 함수
def postfix_notation_str(str,N):
    stack = []
    str_lst = []
    num_lst = [f'{i}' for i in range(10)] # 숫자 리스트(문자)
    for i in range(N): # 문자열 길이만큼 돌아감
        if str[i] in num_lst: # 문자가 숫자리스트 안에 있다면
            str_lst.append(int(str[i])) # 후위 표기법 리스트에 추가
        elif str[i] =='+': # 문자가 +라면
            if (stack and stack[-1] != '*') or not stack:
                stack.append('+') # 스택 마지막이 *이 아니거나 / 스택이 비어있지 않다면 +추가
            else: # stack 안에 top이 +라면 * 전까지 pop하며 후위 표기법 리스트에 추가
                while stack:
                    str_lst.append(stack.pop())
                    if not stack: # 스택이 비었다면 그만
                        break
                    elif len(stack) == 2 and stack[-1] == '*' and stack[-1] =='+':
                        str_lst.append(stack.pop())
                        break
                stack.append('+') # 끝내면서 현재 문자인 + 스택에 추가
        elif str[i] == '*':
            stack.append('*') # *은 stack에 추가
    if stack: # 만약 stack에 남은게 있다면 모두 pop후 후위 표기법 리스트에 추가
        for _ in range(len(stack)):
            str_lst.append(stack.pop())
    return str_lst

# 후위 표기법 계산 함수
def postfix_notation(str_lst):
    stack = []
    for i in range(len(str_lst)):
        if type(str_lst[i]) == int: # 만약 숫자라면
            stack.append(str_lst[i]) # 스택에 추가
        elif str_lst[i] == '+': # 만약 +라면
            b = stack.pop() # 스택 안의 두 숫자를 뽑아
            a = stack.pop() # 더해주고 스택에 다시 넣어주기
            stack.append(a+b)
        elif str_lst[i] == '*': # 만약 *라면
            b = stack.pop() # 스택 안의 두 숫자를 뽑아
            a = stack.pop() # 곱해주고 스택에 다시 넣어주기
            stack.append(a*b)
    return stack[0] # 스택 마지막숫자 return

for tc in range(1, T + 1):
    N = int(input()) # 문자열 길이 입력
    str = input() # 문자열 입력
    a = postfix_notation_str(str,N) # 수식을 후위표기법으로 변환
    print(f'#{tc} {postfix_notation(a)}') # 후위표기법을 계산한 것을 return