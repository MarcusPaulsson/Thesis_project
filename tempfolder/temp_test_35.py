def max_groups(test_cases):
    results = []
    for e in test_cases:
        e.sort()
        count = 0
        group_size = 0
        
        for inexperience in e:
            group_size += 1
            if group_size >= inexperience:
                count += 1
                group_size = 0
        
        results.append(count)
    
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    index = 0
    T = int(data[index])
    index += 1
    test_cases = []
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        e = list(map(int, data[index:index + N]))
        index += N
        test_cases.append(e)
    
    results = max_groups(test_cases)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()