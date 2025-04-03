def process_test_case(n, k, s):
    operations = []
    # We need to create a valid bracket sequence with exactly k regular prefixes
    # We can build it starting from the first `k` pairs of `()`
    target = "()" * k + "()" * (n // 2 - k)
    
    # To achieve the target, we can iterate and fix mismatches by reversing segments
    s = list(s)
    target = list(target)
    
    # Create a pointer for the target sequence
    target_index = 0
    
    for i in range(n):
        if s[i] != target[target_index]:
            # Find the position `j` of the target character in the remaining string
            for j in range(i + 1, n):
                if s[j] == target[target_index]:
                    # We found the character we need to swap into position `i`
                    operations.append((i + 1, j + 1))  # Store 1-based index
                    s[i:j + 1] = s[i:j + 1][::-1]  # Reverse the substring
                    break
        target_index += 1
    
    # Print the number of operations and the operations themselves
    print(len(operations))
    for l, r in operations:
        print(l, r)

# Read the input
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    process_test_case(n, k, s)