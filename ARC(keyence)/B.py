from collections import Counter
N, K = map(int, input().split())
a = list(map(int, input().split()))

# min(K,a.count(0))が利用するべき箱の数
# なるべく連続して数字を確保するゲームか？　貪欲法でいけるか？

counts = Counter(a)
counts = sorted(counts.items(), key=lambda x:x[0])

ans = 0
minnum = K
preind = 0
prenum = 0
diffn = 0

# 0が一個もないなら0
if counts[0][0]!=0:
    print(0)
    exit()

for count in counts:
    thisind = count[0]
    thisnum = count[1]
    diffn = minnum - thisnum
    minnum = min(minnum, thisnum)
    
    # 1個でも存在しない数字があったら即終了
    if (thisind - preind)>=2:
        ans += (preind+1)*prenum
        print(ans)
        exit()

    # 数字の数が減ったら脱落
    if diffn > 0:
        ans += diffn*thisind 
        
    preind = thisind
    prenum = minnum

ans += (preind+1)*minnum
print(ans)

