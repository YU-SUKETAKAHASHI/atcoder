N , W = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]


AB_sorted = sorted(AB, key=lambda x: x[0], reverse=True)

nokori_w = W
oisisa = 0
for A, B in AB_sorted:
    if nokori_w >= B:
        oisisa += A*B
        nokori_w -= B
    elif (nokori_w < B) and (nokori_w > 0):
        oisisa += A*nokori_w
        nokori_w = 0
    else:
        break

print(oisisa)