import numpy as np
N, M = map(int,input().split())

if M: # M!=0のとき
  
  if N==M:
    print(0)
  else:
    a = sorted(list(map(int,input().split())))
    a.insert(0, 0)
    a.append(N+1)
    #print(a)

    seq = [a[i+1]-a[i]-1 for i in range(len(a)-1)]
    #print(seq)

    seq = list(filter(lambda x: x>0 ,seq))
    #print(seq)

    
    k = min(seq)
    #print("k=",k)

    ans = 0
    for s in seq:
      #ans += s//k + s%k　
      #こう書けば良かった　ans += s//k + 1 if s%k else s//k
      ans += np.ceil(s/k) # なんで天井関数使わないと怒られるの？？？
    print(int(ans))
    
else: # M=0のときは1回
  print(1)