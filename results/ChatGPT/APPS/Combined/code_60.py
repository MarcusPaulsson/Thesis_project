def has_palindrome_subsequence(test_cases):
    results = []
    
    for n, a in test_cases:
        seen = {}
        found = False
        
        for i in range(n):
            if a[i] in seen and i - seen[a[i]] >= 2:
                found = True
                break
            seen[a[i]] = i
        
        results.append("YES" if found else "NO")
    
    return results

def main():
    t = int(input())
    test_cases = [(
        int(input()),
        list(map(int, input().split()))
    ) for _ in range(t)]

    results = has_palindrome_subsequence(test_cases)

    print("\n".join(results))

if __name__ == "__main__":
    main()