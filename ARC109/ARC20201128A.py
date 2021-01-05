a,b,x,y = map(int,input().split())

# 絶対に一回は廊下を渡る
# 階段一回上るのは廊下を二回渡るのと同じ

if a > b:
    kaisa = a - b
    if 2*x >= y :
        ans = x + (kaisa-1)*y
    else:
        ans = x + (kaisa-1)*2*x
else:
    kaisa = b - a
    if 2*x >= y :
        ans = x + kaisa*y
    else:
        ans = x + kaisa*2*x

print(ans)


