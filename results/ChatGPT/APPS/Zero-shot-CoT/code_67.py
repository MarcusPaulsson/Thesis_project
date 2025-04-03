def swap_to_equal(k, test_cases):
    results = []
    for case in test_cases:
        n, s, t = case
        indices_s = {}
        indices_t = {}
        
        for i in range(n):
            if s[i] not in indices_s:
                indices_s[s[i]] = []
            if t[i] not in indices_t:
                indices_t[t[i]] = []
            indices_s[s[i]].append(i + 1)
            indices_t[t[i]].append(i + 1)
        
        swaps = []
        # Identify mismatches
        mismatches = []
        for i in range(n):
            if s[i] != t[i]:
                mismatches.append(i + 1)
        
        if not mismatches:
            results.append("Yes\n0")
            continue
        
        # Try to resolve mismatches
        for i in mismatches:
            char_in_s = s[i-1]
            char_in_t = t[i-1]
            
            if char_in_t in indices_s and indices_s[char_in_t]:
                # We can swap the needed character directly
                swap_index = indices_s[char_in_t].pop()
                swaps.append((swap_index, i))
                s[swap_index - 1], t[i - 1] = t[i - 1], s[swap_index - 1]
            elif char_in_s in indices_t and indices_t[char_in_s]:
                # Swap to get char_in_s into t
                swap_index = indices_t[char_in_s].pop()
                swaps.append((i, swap_index))
                s[i - 1], t[swap_index - 1] = t[swap_index - 1], s[i - 1]
                # Now we can do the second swap to fix the original mismatch
                swaps.append((swap_index, i))
                s[swap_index - 1], t[i - 1] = t[i - 1], s[swap_index - 1]
            else:
                results.append("No")
                break
        else:
            results.append("Yes")
            results.append(str(len(swaps)))
            results.extend(f"{x} {y}" for x, y in swaps)
    
    print("\n".join(map(str, results)))

# Read input
k = int(input())
test_cases = []
for _ in range(k):
    n = int(input())
    s = input().strip()
    t = input().strip()
    test_cases.append((n, s, t))

swap_to_equal(k, test_cases)