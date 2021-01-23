N , X = map(int, input().split())
VP = [list(map(int, input().split())) for _ in range(N)]

X = 100*X
x = 0
for i, vp in enumerate(VP, 1):
    x += vp[0]*vp[1]
    if x > X:
        print(i)
        exit()
print(-1)