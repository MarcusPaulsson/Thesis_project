def f(x):
    return x // 10 if x % 10 == 0 else x + 1

def reachable_count(n):
    reachable = set()
    while n not in reachable:
        reachable.add(n)
        n = f(n)
    return len(reachable)

n = int(input())
print(reachable_count(n))