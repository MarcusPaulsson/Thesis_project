def max_coins(N):
    # The maximum coins Mr. Chanek can guarantee to take
    # is determined by whether N is odd or even.
    # If N is odd, he can take (N // 2) coins.
    # If N is even, he can take (N // 2) coins as well.
    return N // 2

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        N = int(data[i])
        results.append(max_coins(N))
    
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()