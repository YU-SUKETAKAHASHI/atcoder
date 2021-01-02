N = int(input())
l = [input() for _ in range(N)]

l_uniq = list(set(l))
l_uniq_ = ["!"+l for l in l_uniq]


intersect = set(l_uniq)&set(l_uniq_)
if intersect:
    print(list(intersect)[0][1:])
else:
    print("satisfiable ")