N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for num, i in enumerate(L):
    for j in L[num+1:]:
        angle = abs(i[1]-j[1])/abs(i[0]-j[0])
        if abs(angle)<=1:
            ans += 1

print(ans)