A,B = input().split(" ")
B_index = 0
A_index = 0
for i in range(len(A)):
    if A[i] in B :
        B_index = B.find(A[i])
        A_index = i
        break

for i in range(len(B)):
    for j in range(len(A)):
        if i == B_index :
            print(A, end="")
            break
        if j == A_index :
            print(B[i],end="")
        else :
            print(".", end="")
    print("")
