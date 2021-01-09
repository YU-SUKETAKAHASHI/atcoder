import numpy as np

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]


L = np.array(L)
# L = np.unique(L, axis=0)

aset = set(L[:, 0])
alist = L[:, 0]
bset = set(L[:, 1])
# blist = L[:,1]
allset = aset | bset
defset = allset - aset
# print(defset)
# print(allset)
# print(aset)
# print(bset)

b = 0
for i, difn in enumerate(defset):
    nindex = np.where(L[:, 1]==difn)[0]
    a = []
    for ind in nindex:
        a.append(len(np.where(alist==alist[ind])[0])-1)
    a = np.array(a)
    if not a.sum():
        b += 1


# print(b)
print(len(allset)-b)
# 全体のユニークな数を数える
# それが 