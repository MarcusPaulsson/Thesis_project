def count_classy_integers(L, R):
    classy_count = 0
    for num in range(L, R + 1):
        if len([d for d in str(num) if d != '0']) <= 3:
            classy_count += 1
    return classy_count

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        L, R = map(int, data[i].split())
        result = count_classy_integers(L, R)
        results.append(result)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()