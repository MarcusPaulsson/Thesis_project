def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    k = int(data[0])
    index = 1
    results = []
    
    for _ in range(k):
        n = int(data[index])
        s = list(data[index + 1])
        t = list(data[index + 2])
        index += 3
        
        # Count frequency of characters in both strings
        from collections import Counter
        count_s = Counter(s)
        count_t = Counter(t)
        
        # Check if we can make strings equal
        total_count = count_s + count_t
        
        # If any character has an odd total frequency, it's impossible to match
        if any(count % 2 != 0 for count in total_count.values()):
            results.append("No")
            continue
        
        results.append("Yes")
        swaps = []

        # Create a list of indices of mismatched characters
        mismatch_s = []
        mismatch_t = []

        for i in range(n):
            if s[i] != t[i]:
                mismatch_s.append(i)
                mismatch_t.append(i)

        # Making the strings equal
        while mismatch_s:
            i = mismatch_s.pop()
            j = mismatch_t.pop()
            
            # If characters at these positions are already equal, continue
            if s[i] == t[j]:
                continue
            
            # Swap s[i] with t[j]
            swaps.append((i + 1, j + 1))  # Store 1-based index
            s[i], t[j] = t[j], s[i]
            
            if s[i] != t[i]:  # Check if we need to fix s[i]
                mismatch_s.append(i)
            if s[j] != t[j]:  # Check if we need to fix t[j]
                mismatch_t.append(j)

        # Output result
        results.append(str(len(swaps)))
        for swap in swaps:
            results.append(f"{swap[0]} {swap[1]}")
    
    print("\n".join(results))

# Uncomment the below line to run the function when executing this script
# solve()