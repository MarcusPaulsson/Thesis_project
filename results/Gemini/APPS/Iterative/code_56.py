def f(x):
    x += 1
    while x % 10 == 0:
        x //= 10
    return x

def solve():
    n = int(input())
    reachable = set()
    curr = n
    while curr not in reachable:
        reachable.add(curr)
        curr = f(curr)
    print(len(reachable))

solve()