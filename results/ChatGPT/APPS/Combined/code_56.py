def remove_trailing_zeros(x):
    """Increment x by 1 and remove trailing zeros."""
    x += 1
    while x % 10 == 0:
        x //= 10
    return x

def count_reachable_numbers(n):
    """Count how many different numbers are reachable from n using the function f."""
    reachable_numbers = set()
    current = n
    
    while current not in reachable_numbers:
        reachable_numbers.add(current)
        current = remove_trailing_zeros(current)
    
    return len(reachable_numbers)

if __name__ == "__main__":
    n = int(input().strip())
    print(count_reachable_numbers(n))