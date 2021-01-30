# pypy3でやった
N = int(input())

cumsum = [0]*10**7
for i in range(1, 10**7):
  cumsum[i] = cumsum[i-1] + i
  
ans = 0
for i in range(10**7-1):
    cs = cumsum[i+1]
    if (N-cs)%(i+1) == 0:
        ans += 2
    
    if cs >= N:
        exit(print(ans))
