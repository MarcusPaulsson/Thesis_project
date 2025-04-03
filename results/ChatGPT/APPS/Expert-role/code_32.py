def maximum_coins(n):
    # If n is odd, Mr. Chanek can only take one coin
    if n % 2 == 1:
        return n // 2
    # If n is even, he can take half
    else:
        return n // 2

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        N = int(data[i])
        results.append(maximum_coins(N))
    
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()