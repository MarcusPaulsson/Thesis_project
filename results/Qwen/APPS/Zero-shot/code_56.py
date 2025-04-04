def count_reachable_numbers(n):
    reachable_numbers = set()
    while n not in reachable_numbers:
        reachable_numbers.add(n)
        n += 1
        while n % 10 == 0:
            n //= 10
    return len(reachable_numbers)

n = int(input())
print(count_reachable_numbers(n))