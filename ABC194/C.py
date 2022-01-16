N = int(input())
A = list(map(int, input().split()))

# err = sum((A[i] - A[j])**2 for i in range(1,N) for j in range(i))
# print(err)

import numpy as np

A = sorted(A)
A_diff = [A[i+1]-A[i] for i in range(N-1)]
# A_comsum = []
# for diff in A_diff:
#     A_comsum.append()
err = 0
for i in range(len(A_diff)):
    A_comsum = np.cumsum(A_diff[i:])
    err += (np.array(A_comsum)**2).sum()

print(err)
