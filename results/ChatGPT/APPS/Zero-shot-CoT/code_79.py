def get_divisors(n):
    divisors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        divisors = get_divisors(n)
        divisors.sort()
        
        # Initial order of divisors
        initial_order = divisors
        
        # Determine the minimal moves needed
        if len(initial_order) == 2:
            # Two divisors are always non-coprime (since n is composite)
            moves = 0
        else:
            # For three or more divisors, we can always arrange them to avoid coprime adjacencies
            moves = 0
            
        results.append(" ".join(map(str, initial_order)))
        results.append(str(moves))
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()