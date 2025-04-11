def f(x):
    x += 1
    while x % 10 == 0:
        x //= 10
    return x

def solve():
    n = int(input())
    reachable = set()
    reachable.add(n)
    
    current = n
    while True:
        current = f(current)
        if current in reachable:
            break
        reachable.add(current)
    
    print(len(reachable))

solve()