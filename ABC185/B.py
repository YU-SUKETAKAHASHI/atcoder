N, M, T = map(int,input().split())
n = N

a = []
b = []
for i in range(M):
  a_, b_ = map(int,input().split())
  a.append(a_)
  b.append(b_)     

alive = True
for i in range(M):
  n -= a[i] if i==0 else a[i] - b[i-1]
  #print("お店に着いた！ n: ", n)
  if n <= 0:
    print("No")
    alive = False
    break
    
  n += b[i] - a[i]
  n = min(n, N)
  #print("お店から出た！ n: ", n)
  
# お店から出たあと
#print("家についた！ n:", n-(T-b[M-1]))
if n-(T-b[M-1])>0 & alive:
  print("Yes")
elif (n-(T-b[M-1])<=0) & alive:
  print("No")