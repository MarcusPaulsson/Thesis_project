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
    data = input().splitlines()
    
    T = int(data[0])
    index = 1
    test_cases = []
    
    for _ in range(T):
        N = int(data[index])
        explorers = list(map(int, data[index + 1].split()))
        test_cases.append(explorers)
        index += 2
        
    results = max_groups(test_cases)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()