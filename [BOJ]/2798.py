N, M = map(int, input().split())
cards = list(map(int, input().split()))

temp = 0
result = 0
save = 0
max_val = 300001
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            result = cards[i] + cards[j] + cards[k]
            temp = abs(M-result)
            if result <= M and max_val > temp:
                max_val = temp
                save = result
print(save)
