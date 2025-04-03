def max_operations(t, test_cases):
    results = []
    for n, s in test_cases:
        count_0 = 0
        count_1 = 0
        # Count the number of segments of 1s and 0s
        current_char = s[0]
        if current_char == '0':
            count_0 += 1
        else:
            count_1 += 1

        for char in s[1:]:
            if char != current_char:
                if char == '0':
                    count_0 += 1
                else:
                    count_1 += 1
                current_char = char
        
        results.append(min(count_0, count_1) + 1)

    return results

# Example Usage
t = int(input())
test_cases = [(int(input()), input().strip()) for _ in range(t)]
results = max_operations(t, test_cases)
for result in results:
    print(result)