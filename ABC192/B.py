S = input()

odd = ''.join([s for i, s in enumerate(S, 1) if i%2==1])
eve = ''.join([s for i, s in enumerate(S, 1) if i%2==0])

print('Yes') if odd==odd.lower() and eve==eve.upper() else print('No')
