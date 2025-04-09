def sum_digits(n):
    """Calculates the sum of the digits of a non-negative integer."""
    s = str(n)
    return sum(int(digit) for digit in s)


def solve():
    """Finds the largest integer <= x with the maximum sum of digits."""
    x = int(input())
    x_str = str(x)
    n = len(x_str)

    best_num = x
    best_sum = sum_digits(x)

    for i in range(n):
        if x_str[i] == '0':
            continue

        num_str = x_str[:i] + str(int(x_str[i]) - 1) + '9' * (n - i - 1)
        num = int(num_str)

        if num >= 0:  # Ensure num is non-negative
            current_sum = sum_digits(num)
            if current_sum > best_sum:
                best_sum = current_sum
                best_num = num
            elif current_sum == best_sum and num > best_num:
                best_num = num

    print(best_num)


if __name__ == "__main__":
    solve()