import numpy as np

N = int(input())
A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

if not np.dot(A, B):
    print("Yes")
else:
    print("No")

