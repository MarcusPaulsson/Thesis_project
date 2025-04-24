def sum_digits(n):
    """Calculates the sum of the digits of a non-negative integer.

    Args:
        n: The non-negative integer.

    Returns:
        The sum of the digits of n.
    """
    s = str(n)
    sum_val = 0
    for digit in s:
        sum_val += int(digit)
    return sum_val


def solve():
    """Finds the largest integer not exceeding x with the maximum sum of digits."""
    x = int(input())

    best_num = x
    max_sum = sum_digits(x)

    s = str(x)
    n = len(s)

    for i in range(n):
        if s[i] == '0':
            continue

        num_str = s[:i] + str(int(s[i]) - 1) + '9' * (n - i - 1)
        num = int(num_str)

        if num > 0:
            current_sum = sum_digits(num)
            if current_sum > max_sum:
                max_sum = current_sum
                best_num = num
            elif current_sum == max_sum and num > best_num:
                best_num = num

    print(best_num)


if __name__ == "__main__":
    solve()