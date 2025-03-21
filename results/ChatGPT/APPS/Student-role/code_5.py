def find_permutations(t, test_cases):
    results = []
    
    for case in test_cases:
        n, a = case
        count = [0] * (n + 1)
        total_unique = 0
        
        # Count occurrences of each number
        for num in a:
            count[num] += 1
        
        ways = []
        
        # Check for possible splits
        for l1 in range(1, n):
            l2 = n - l1
            
            # Count unique numbers in first l1 elements
            unique_count_p1 = 0
            valid = True
            
            for i in range(l1):
                if count[a[i]] == 1:
                    unique_count_p1 += 1
                elif count[a[i]] > 1:
                    valid = False
                    break
            
            if valid and unique_count_p1 == l1:
                # Count unique numbers in last l2 elements
                unique_count_p2 = 0
                valid = True
                
                for i in range(l1, n):
                    if count[a[i]] == 1:
                        unique_count_p2 += 1
                    elif count[a[i]] > 1:
                        valid = False
                        break
                
                if valid and unique_count_p2 == l2:
                    ways.append((l1, l2))
        
        results.append(ways)
    
    output = []
    for ways in results:
        output.append(str(len(ways)))
        for l1, l2 in ways:
            output.append(f"{l1} {l2}")
    
    return "\n".join(output)

# Reading input
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

# Getting results
result = find_permutations(t, test_cases)

# Printing results
print(result)