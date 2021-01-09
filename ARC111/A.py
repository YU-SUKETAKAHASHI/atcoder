import numpy as np

N,M = map(int, input().split())

def pow_r(x, n):
    """
    O(log n)
    """
    print(x)
    if n == 0:  # exit case
        return 1
    # elif n % 10000 == 0:
    #     return pow_r(x ** 10000, n // 10000)
    # elif n % 1000 == 0:
    #     return pow_r(x ** 1000, n // 1000)
    # elif n % 100 == 0:
    #     return pow_r(x ** 100, n // 100)
    # elif n % 10 == 0:
    #     return pow_r(x ** 10, n // 10)
    elif n % 2 == 0:  # standard case ① n is even
        return pow_r(x ** 2, n // 2)
    elif n % 2 == 1:  # standard case ② n is odd
        return x * pow_r(x ** 2, (n - 1) // 2)


def pow_k(x, n):
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
        x *= x
        n //= 2

    return K * x


ans = np.exp(N*np.log(10)-np.log(M))



# ans = np.floor((10**N)/M)%M

# pow10N = pow_k(10, N)
# pow10N = np.power(10,N)

# ans = (pow10N//M)%M
print(ans)

