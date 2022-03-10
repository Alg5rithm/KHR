N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A배열은 오름차순, B배열은 내림차순으로 정렬한다.
# sort라이브러리는 퀵 정렬을 기반으로 하므로 O(NlogN)만큼 시간소요
A.sort()
B.sort(reverse=True)
print(A, B)

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i] , A[i]
    else:
        break
print(sum(A))
