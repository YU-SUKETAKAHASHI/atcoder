N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ab = []
maxa = 0
maxab = 0
for i in range(N):
    maxa = max(A[i], maxa)
    maxab = max(maxa*B[i], maxab)
    print(maxab)