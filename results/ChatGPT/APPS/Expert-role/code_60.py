def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        a, b = map(int, data[i].split())
        results.append(a ^ b)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    solve()