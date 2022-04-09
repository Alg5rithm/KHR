
while True:
    s = input()
    if s == '.':
        break
    
    flag = True
    stack = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
        elif s[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break
        elif s[i] == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = False
                break

    if flag and not stack :
        print("yes")
    else:
        print("no")
