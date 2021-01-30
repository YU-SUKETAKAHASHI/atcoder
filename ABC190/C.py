N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [list(map(int, input().split())) for _ in range(K)]

maxans = 0
for i in range(2**K):
    flag = []
    for j in range(K):
        if ((i >> j) & 1):
            flag.append(CD[j][0])
        else:
            flag.append(CD[j][1])
    ans = 0
    for ab in AB:
        if (ab[0] in flag) and (ab[1] in flag):
            ans += 1
    maxans = max(ans, maxans)

print(maxans)
