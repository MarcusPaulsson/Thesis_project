from collections import Counter

def main():
    n = int(input("Enter the number of divisors: "))
    divisors = list(map(int, input("Enter the divisors: ").split()))

    if n != len(divisors):
        print("Error: The number of divisors provided does not match the count.")
        return

    # Count occurrences of each divisor
    count = Counter(divisors)

    # The product of the unique divisors
    unique_divisors = set(divisors)
    x_y_product = 1
    for d in unique_divisors:
        x_y_product *= d

    # x is the maximum divisor, y is calculated as the product divided by x
    x = max(unique_divisors)
    y = x_y_product // x if x != 0 else 0

    print(x, y)

if __name__ == "__main__":
    main()