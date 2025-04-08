def remove_trailing_zeros(x):
    while x % 10 == 0:
        x //= 10
    return x

def f(x):
    return remove_trailing_zeros(x + 1)

def count_reachable_numbers(n):
    reachable = set()
    current = n
    
    while current not in reachable:
        reachable.add(current)
        current = f(current)
    
    return len(reachable)

if __name__ == "__main__":
    n = int(input().strip())
    print(count_reachable_numbers(n))