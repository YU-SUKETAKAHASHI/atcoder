# 通ってない

import numpy as np

N, C = list(map(int, input().split()))
L = np.array([np.array(list(map(int, input().split())), dtype="float128") for _ in range(N)], dtype="float128")

a = L[:,0]
b = L[:,1]
c = L[:,2]

kikan = np.sort(np.concatenate([a, b]))

nissuu = [kikan[i+1]-kikan[i]+1 for i in range(len(kikan)-1)]
nissuu.append(0)
nissuu = np.array(nissuu, dtype="float128")


flag = np.zeros((N, len(kikan)))
for i in range(N):
    flag[i] = np.array([1 if (a[i]<=k and k<b[i]) else 0 for k in kikan], dtype="float128")

flag = flag.T
kikanmoney = flag * c
kikanmoney = kikanmoney.sum(axis=1)

ans = 0
for i in range(len(kikan)):
    if kikanmoney[i]<=C:
        ans += kikanmoney[i] * nissuu[i]
    else:
        ans += C * nissuu[i]
print(ans)