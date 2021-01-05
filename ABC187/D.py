import numpy as np

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

L_di = [2*l[0]+l[1] for l in L]
L_di_sorted = sorted(L_di, reverse=True)

aoki = np.sum(L, axis=0)[0]

for i in range(N):
    aoki -= L_di_sorted[i]
    if aoki<0:
        print(i+1)
        break 


