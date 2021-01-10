import numpy as np
import copy

N = int(input())
A = list(map(int, input().split()))

Acopy = copy.deepcopy(A)

for n in range(N-1):
    A = [max(A[2*i], A[2*i+1]) for i in range(2**(N-n-1))]

min_ = min(A[0], A[1])

for i, a in enumerate(Acopy, 1):
    if a==min_:
        print(i)
        exit()