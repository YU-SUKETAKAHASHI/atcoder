import numpy as np
from decimal import Decimal

X, Y, R = map(Decimal, input().split())

ans = 0
for x_ in range(np.ceil(X-R), np.floor(X+R)+1):
    top = np.floor(Y+ (R**2 - (X-x_)**2).sqrt())
    bottom = np.ceil(Y-(R**2 - (X-x_)**2).sqrt()) 
    ans += top - bottom + 1
print(ans)

# # ============================================
# X, Y, R = map(float, input().split())
# X = int(1000*X)
# Y = int(1000*Y)
# R = int(1000*R)

# x = [*range(low, high+1)]