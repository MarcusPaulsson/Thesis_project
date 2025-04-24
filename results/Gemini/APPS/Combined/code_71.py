import math

def solve():
    """
    Calculates the smallest integer k such that 2^k >= a.

    This function takes an integer 'a' as input and calculates the smallest
    integer 'k' such that 2 raised to the power of 'k' is greater than or
    equal to 'a'.  It handles the special case where a = 1 directly and
    uses the ceiling of the base-2 logarithm for other values of 'a'.

    """
    a = int(input())
    if a == 1:
        print(1)
    else:
        print(math.ceil(math.log2(a)))

solve()