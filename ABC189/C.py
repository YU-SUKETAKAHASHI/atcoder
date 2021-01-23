N = int(input())
A = list(map(int, input().split()))

max_ = 0
for l in range(N):
    min_ = A[l]
    for r in range(l, N):
        min_ = min(min_, A[r])
        max_ = max(max_, min_*(r-l+1))

print(max_)