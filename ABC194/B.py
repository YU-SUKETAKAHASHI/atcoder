N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

A = [l[0] for l in L]
B = [l[1] for l in L]

minA = min(A)
minB = min(B)

min2A = sorted(A)[1]
min2B = sorted(B)[1]

minA_index = [i for i, a in enumerate(A) if a == minA]
minB_index = [i for i, b in enumerate(B) if b == minB]

if len(minA_index)==1 and len(minB_index)==1 and minA_index[0]==minB_index[0]:
    if (minA + minB) <= min(min2A, min2B):
        print(minA + minB)
    else:
        print(max(min(min2A, min2B), max(minA, minB)))
else:
    print(max(minA, minB))

