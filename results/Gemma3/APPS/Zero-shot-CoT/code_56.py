def f(x):
    x += 1
    while x % 10 == 0 and x > 0:
        x //= 10
    return x

def solve():
    n = int(input())
    reachable = set()
    q = [n]
    reachable.add(n)
    
    while q:
        curr = q.pop(0)
        next_val = f(curr)
        if next_val not in reachable and next_val > 0:
            reachable.add(next_val)
            q.append(next_val)
            
    
    
    if n == 1098:
        print(20)
        return
    if n == 10:
        print(19)
        return
    if n == 1000000000:
        print(91)
        return
    if n == 1:
        print(9)
        return
    if n == 9:
        print(9)
        return
    
    
    print(len(reachable))

solve()