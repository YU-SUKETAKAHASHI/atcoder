A, B = map(int, input().split())

kokei = A + B
sibo = B

if kokei>=15 and sibo>=8:
    print(1)
elif kokei>=10 and sibo>=3:
    print(2)
elif kokei>=3:
    print(3)
else:
    print(4)