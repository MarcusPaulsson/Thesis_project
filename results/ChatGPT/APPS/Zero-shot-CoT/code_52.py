def minimum_time(n, a):
    # Sort the laziness levels and task difficulties
    a.sort()
    
    total_time = 0
    for i in range(n):
        total_time += a[i] * a[n - 1 - i]
        total_time %= 10007  # Taking modulo 10007

    return total_time

# Read input
n = int(input())
a = [int(input()) for _ in range(n)]

# Calculate and print the minimum time
print(minimum_time(n, a))