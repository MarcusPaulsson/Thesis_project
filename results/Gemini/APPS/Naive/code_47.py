def max_beauty(n, x, a):
    """
    Calculates the maximum possible beauty of an array after multiplying at most one consecutive subarray by x.

    Args:
        n: The length of the array.
        x: The multiplier for the subarray.
        a: The array of integers.

    Returns:
        The maximum possible beauty of the array.
    """

    max_so_far = 0
    for i in range(n + 1):
        for j in range(i, n + 1):
            temp_a = a[:]
            for k in range(i, j):
                temp_a[k] *= x

            current_max = 0
            max_ending_here = 0
            for val in temp_a:
                max_ending_here = max(0, max_ending_here + val)
                current_max = max(current_max, max_ending_here)

            max_so_far = max(max_so_far, current_max)

    return max_so_far


if __name__ == "__main__":
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(max_beauty(n, x, a))