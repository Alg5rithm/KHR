
s = input()

result = 0

for i in range(0, len(s)):
    num = int(s[i])
    
    if result == 0 or result+num > result*num :
        result += num
    else :
        result *= num
print(result)
