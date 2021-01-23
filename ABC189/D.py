N = int(input())
S = [input() for _ in range(N)]

# 後ろから逆算して行ったほうがよさそう
# 漸化式みたいに考えられそう

def logical(bools, n):
    if n != 0:
        b = bools.pop()
        if b == 'OR':
            return 2**(n) + logical(bools, n-1)
        elif b == 'AND':
            return logical(bools, n-1)
    else:
        return 1

ans = logical(S, N)
print(ans)