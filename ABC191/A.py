V, T, S, D = map(int, input().split())

if D<V*T or S*V<D:
    print('Yes')
else:
    print('No')