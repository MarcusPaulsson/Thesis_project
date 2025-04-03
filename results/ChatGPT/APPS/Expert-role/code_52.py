def minimum_total_time(n, a):
    a.sort()
    total_time = 0
    
    for i in range(n):
        total_time += a[i] * a[n - 1 - i]
        total_time %= 10007
        
    return total_time

# Input handling
n = int(input())
a = [int(input()) for _ in range(n)]

# Calculate and print the result
result = minimum_total_time(n, a)
print(result)