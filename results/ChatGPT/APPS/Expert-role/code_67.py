def can_make_equal(s, t):
    # Count characters in both strings
    count_s = {}
    count_t = {}
    
    for char in s:
        count_s[char] = count_s.get(char, 0) + 1
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1
    
    # Check if they can be made equal by ensuring that combined counts are even
    for char in set(s + t):
        if (count_s.get(char, 0) + count_t.get(char, 0)) % 2 != 0:
            return False, []
    
    swap_operations = []
    s = list(s)
    t = list(t)
    
    # Create lists to store positions of mismatches
    s_mismatches = []
    t_mismatches = []
    
    for i in range(len(s)):
        if s[i] != t[i]:
            s_mismatches.append(i)
            t_mismatches.append(i)
    
    # Now we can perform swaps to fix mismatches
    for i in range(len(s_mismatches)):
        if s[s_mismatches[i]] != t[s_mismatches[i]]:
            # Find a character in s that matches the t's character at the current mismatch
            if s_mismatches[i] < len(s):
                swap_operations.append((s_mismatches[i] + 1, s_mismatches[i] + 1))  # Swap with itself for convenience
                swap_operations.append((s_mismatches[i] + 1, t.index(s[s_mismatches[i]]) + 1))  # Swap with t
            if t_mismatches[i] < len(t):
                swap_operations.append((t_mismatches[i] + 1, t_mismatches[i] + 1))  # Swap with itself for convenience
                swap_operations.append((t_mismatches[i] + 1, s.index(t[t_mismatches[i]]) + 1))  # Swap with s
    
    return True, swap_operations[:2 * len(s_mismatches)]

import sys
input = sys.stdin.read

data = input().splitlines()
k = int(data[0])
index = 1
results = []

for _ in range(k):
    n = int(data[index])
    s = data[index + 1]
    t = data[index + 2]
    index += 3
    
    can_equal, operations = can_make_equal(s, t)
    
    if can_equal:
        results.append("Yes")
        results.append(str(len(operations)))
        results.extend(f"{i} {j}" for i, j in operations)
    else:
        results.append("No")

print("\n".join(results))