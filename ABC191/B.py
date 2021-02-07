N, X = map(int, input().split())
A = input()

# A_ = []
# for a in A:
#     if a != X:
#         A_.append(a)

A = [a for a in A if a!=X]

# A = A.replace(str(X), '')
# A = A.replace('  ', ' ')
print(*A)
