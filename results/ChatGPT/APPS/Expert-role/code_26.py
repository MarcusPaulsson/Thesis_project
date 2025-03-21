def can_solve_puzzle(n, m):
    # The puzzle can be solved if either n or m is odd
    return (n % 2 == 1) or (m % 2 == 1)

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n, m = map(int, data[i].split())
        if can_solve_puzzle(n, m):
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()