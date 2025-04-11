def max_beauty(n, x, a):
    """
    Calculates the maximum possible beauty of array a after multiplying all values
    belonging to some consecutive subarray by x.

    Args:
        n: The length of array a.
        x: The integer to multiply the subarray by.
        a: The array of integers.

    Returns:
        The maximum possible beauty of array a after multiplying all values
        belonging to some consecutive subarray by x.
    """

    max_so_far = 0
    for i in range(n + 1):
        for j in range(i, n + 1):
            current_array = a[:]
            for k in range(i, j):
                current_array[k] *= x

            current_max = 0
            max_ending_here = 0
            for num in current_array:
                max_ending_here = max(0, max_ending_here + num)
                current_max = max(current_max, max_ending_here)

            max_so_far = max(max_so_far, current_max)

    return max_so_far


if __name__ == "__main__":
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    result = max_beauty(n, x, a)
    print(result)