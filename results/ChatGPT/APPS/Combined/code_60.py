def has_palindromic_subsequence(test_cases):
    results = []
    
    for n, a in test_cases:
        last_occurrence = {}
        found_palindrome = False
        
        for i in range(n):
            if a[i] in last_occurrence and i - last_occurrence[a[i]] >= 2:
                found_palindrome = True
                break
            last_occurrence[a[i]] = i
        
        results.append("YES" if found_palindrome else "NO")
    
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    test_cases = []
    
    index = 1
    for _ in range(t):
        n = int(data[index])
        a = list(map(int, data[index + 1].split()))
        test_cases.append((n, a))
        index += 2

    results = has_palindromic_subsequence(test_cases)
    
    print("\n".join(results))

if __name__ == "__main__":
    main()