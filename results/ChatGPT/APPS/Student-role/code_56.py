def f(x):
    x += 1
    while x % 10 == 0:
        x //= 10
    return x

def reachable_count(n):
    reachable = set()
    current = n
    
    while current not in reachable:
        reachable.add(current)
        current = f(current)
    
    return len(reachable)

n = int(input())
print(reachable_count(n))