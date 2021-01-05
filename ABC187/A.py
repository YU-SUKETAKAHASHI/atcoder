a,b = map(int,input().split())

a_str = str(a)
a_sum = int(a_str[0]) + int(a_str[1]) + int(a_str[2])

b_str = str(b)
b_sum = int(b_str[0]) + int(b_str[1]) + int(b_str[2])

print(max(a_sum, b_sum))