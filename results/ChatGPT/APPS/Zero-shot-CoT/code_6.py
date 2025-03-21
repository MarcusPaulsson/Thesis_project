def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    T = int(data[index])
    index += 1
    results = []

    for _ in range(T):
        n, m = map(int, data[index].split())
        index += 1
        
        # We will close the last (4/7)n spots
        k = min(n, (4 * n) // 7)
        # We can safely close the last k spots
        closed_spots = list(range(n - k + 1, n + 1))

        results.append(f"{k}")
        results.append(" ".join(map(str, closed_spots)))

    print("\n".join(results))

if __name__ == "__main__":
    main()