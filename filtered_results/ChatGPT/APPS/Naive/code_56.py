def remove_trailing_zeros(x):
    while x % 10 == 0:
        x //= 10
    return x

def reachable_count(n):
    reachable_numbers = set()
    current = n
    
    while current not in reachable_numbers:
        reachable_numbers.add(current)
        current = remove_trailing_zeros(current + 1)
    
    return len(reachable_numbers)

n = int(input())
print(reachable_count(n))