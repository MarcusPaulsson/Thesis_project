def f(x):
    x += 1
    while x % 10 == 0 and x > 0:
        x //= 10
    return x

def count_reachable(n):
    reachable = set()
    q = [n]
    reachable.add(n)
    
    while q:
        curr = q.pop(0)
        next_val = f(curr)
        if next_val not in reachable and next_val > 0 and next_val <= 10**9:
            reachable.add(next_val)
            q.append(next_val)
            
    return len(reachable)

if __name__ == "__main__":
    n = int(input())
    print(count_reachable(n))