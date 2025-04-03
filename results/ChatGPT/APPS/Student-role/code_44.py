def find_chairs(n):
    # We can take chairs numbered as even numbers from 2 to 4n
    return list(range(2, 4 * n + 1, 2))

t = int(input())
for _ in range(t):
    n = int(input())
    chairs = find_chairs(n)
    print(" ".join(map(str, chairs)))