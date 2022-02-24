n, k = map(int, input().split())
s = input()
li = list(s)
count = 0
for i in range(len(s)):
    if s[i] == 'P' :
        j = i - k
        
        while j <= i + k and j < len(s):
            if j >= 0 :
                if li[j] == 'H':
                    li[j] = 'E'
                    break
            j += 1
        
        
for val in li :
    if val == 'E' :
        count += 1
print(count)

# 1. 사람 - > 왼쪽부터 봐서 가까이에 햄버거가 있으면 먹는다. 
# 2. 먹은 햄버거는 E로 표시한다.
