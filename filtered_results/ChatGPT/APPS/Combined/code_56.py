def count_reachable_numbers(n):
    reachable = set()

    def f(x):
        x += 1
        while x % 10 == 0:
            x //= 10
        return x

    current = n
    while current not in reachable:
        reachable.add(current)
        current = f(current)

    return len(reachable)

n = int(input())
print(count_reachable_numbers(n))