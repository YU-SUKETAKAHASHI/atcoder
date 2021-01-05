import numpy as np

N, W = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]

L = np.array(L)

ans =(L-L.min()).sum()

print(ans)