# import numpy as np
import math
import bisect

n = int(input())


# n - ((n+1)が含む三角数の数) + 1



def search_sque_num(num):
    list_ = list(range(1,num))

    low = 0
    high = num

    t = (low+high)/2

    while True:
        t = (low+high)/2
        
        if t*(t+1)/2 < num:
            low = t+1
        else:
            break

    # 計算誤差で無理だった
    # ans = math.floor(((-1+math.sqrt(1+8*(n+1)))/2))
    
    


    return ans

ans = n - search_sque_num(n) + 1

print(ans)