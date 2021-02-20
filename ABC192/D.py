X = input()
M = int(input())

n = int(max(X))
low = n
high = 1000000000000000001
# high = M + 1　これでもok

if len(X) == 1:
    print(int(int(X) <= M))
else:
    while high - low > 1:
        temp_n = (low + high)//2
        base_n = sum(int(bn)*(temp_n**i) for i, bn in enumerate(X[::-1]))
        if base_n <= M:
            low = temp_n
        elif base_n > M:
            high = temp_n
    print(low-n)