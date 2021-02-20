N, K = map(int, input().split())

def kaprekar(num):
    g1 = ''.join(sorted(str(num), reverse=True))
    g2 = ''.join(sorted(str(num)))
    return int(g1) - int(g2)

for i in range(K):
    N = kaprekar(N)

print(N)