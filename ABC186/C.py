N = int(input())


def Base_10_to_8(X):
    if (int(X/8)):
        return Base_10_to_8(int(X/8))+str(X%8)
    return str(X%8)
    
c10 = 0
c8 = 0
c108 = 0
for i in range(N):
    if '7' in str(i+1):
        c10 += 1
        if '7' in str(Base_10_to_8(i+1)):
            c108 += 1

    if '7' in str(Base_10_to_8(i+1)):
        c8 += 1

ans = N - c10 - c8 + c108
print(ans)