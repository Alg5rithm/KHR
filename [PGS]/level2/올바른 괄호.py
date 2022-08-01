# (가 나오면 스택에 push, )가 나오면 pop
# 단, 스택이 비어있는데 )가 나오면 )를 넣어주고 마지막에 검사 코드를 추가

def solution(s):
    answer = True
    
    temp = []
    for i in range(len(s)):
        if s[i] == '(':
            temp.append('(')
        else:
            if len(temp) == 0:
                temp.append(')')
            else:
                temp.pop()
    if len(temp) != 0:
        answer = False
        
    if len(temp) == 1 :
        if temp[0] == ')':
            answer = False

    return answer
