def minimum_difference(n):
    total_sum = n * (n + 1) // 2
    return total_sum % 2

if __name__ == "__main__":
    n = int(input().strip())
    print(minimum_difference(n))