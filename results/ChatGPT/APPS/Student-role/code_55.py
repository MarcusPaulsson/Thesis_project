def max_equal_length_sticks(n):
    return (n + 1) // 2

t = int(input())
for _ in range(t):
    n = int(input())
    print(max_equal_length_sticks(n))