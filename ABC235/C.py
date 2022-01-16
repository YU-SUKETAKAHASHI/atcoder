from collections import defaultdict

N , Q = map(int, input().split())
A = list(map(int, input().split()))
XK = [list(map(int, input().split())) for _ in range(Q)]


A_dict = defaultdict(list)
for i, a in enumerate(A):
    A_dict[a].append(i+1)

for x, k in XK:
    try:
        print(A_dict[x][k-1])
    except IndexError:
        print(-1)