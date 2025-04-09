def f(x):
    x += 1
    while x % 10 == 0:
        x //= 10
    return x

def solve():
    n = int(input())
    reachable = {n}
    curr = n
    while True:
        curr = f(curr)
        if curr in reachable:
            break
        reachable.add(curr)
    print(len(reachable))

solve()