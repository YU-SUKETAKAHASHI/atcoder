# 切断できるか所は(L-1)か所
# そこから11か所選べばいい
from scipy.special import comb

L = int(input())
print(comb(L-1, 11, exact=True))