def count_from_zero_to_n(n):
    if n < 0:
        raise ValueError('n should be a non-negative integer')
    for x in range(0, n+1):
        print(x)

count_from_zero_to_n(10)
