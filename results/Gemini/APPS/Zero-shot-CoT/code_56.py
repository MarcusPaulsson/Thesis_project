def f(x):
    x += 1
    while x % 10 == 0:
        x //= 10
    return x

def solve():
    n = int(input())
    reachable = {n}
    q = [n]
    
    while q:
        curr = q.pop(0)
        next_val = f(curr)
        if next_val not in reachable:
            reachable.add(next_val)
            q.append(next_val)
            
    print(len(reachable))

solve()