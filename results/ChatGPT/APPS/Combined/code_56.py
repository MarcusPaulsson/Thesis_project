def f(x):
    """Applies the function f to the input x: increments x by 1 and removes trailing zeros."""
    x += 1
    while x % 10 == 0:
        x //= 10
    return x

def count_reachable_numbers(n):
    """Counts how many different numbers are reachable from n using the function f."""
    reachable = set()
    current = n
    
    while current not in reachable:
        reachable.add(current)
        current = f(current)
    
    return len(reachable)

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(count_reachable_numbers(n))