def can_be_sum_of_two_cubes(n):
    lo = 1
    hi = int(n**(1/3))  # Maximum value for the cube root of n

    while lo <= hi:
        curr = lo**3 + hi**3
        if curr == n:
            return True
        elif curr < n:
            lo += 1
        else:
            hi -= 1

    return False

# Driver Code
N = 100  # Example value for N
result = can_be_sum_of_two_cubes(N)