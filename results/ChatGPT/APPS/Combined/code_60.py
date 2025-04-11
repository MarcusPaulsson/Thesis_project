def has_palindrome_subsequence(test_cases):
    results = []
    for n, a in test_cases:
        found = False
        first_occurrence = {}
        
        for i in range(n):
            if a[i] in first_occurrence:
                if i - first_occurrence[a[i]] >= 2:
                    found = True
                    break
            else:
                first_occurrence[a[i]] = i
        
        results.append("YES" if found else "NO")
    
    return results

def main():
    t = int(input())
    test_cases = []
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        test_cases.append((n, a))

    results = has_palindrome_subsequence(test_cases)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()