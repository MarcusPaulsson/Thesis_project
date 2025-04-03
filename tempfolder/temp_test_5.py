def count_permutations(t, test_cases):
    results = []
    
    for n, a in test_cases:
        count = [0] * (n + 1)
        for num in a:
            count[num] += 1
        
        left_set, right_set = set(), set()
        k = 0
        ways = []
        
        for i in range(n):
            left_set.add(a[i])
            count[a[i]] -= 1
            
            if count[a[i]] == 0:
                right_set.add(a[i])
                
            l1 = i + 1
            l2 = n - l1
            
            if len(left_set) == l1 and len(right_set) == l2:
                k += 1
                ways.append((l1, l2))
        
        results.append((k, ways))
    
    return results

# Input handling
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

results = count_permutations(t, test_cases)

# Output
output = []
for k, ways in results:
    output.append(str(k))
    for l1, l2 in ways:
        output.append(f"{l1} {l2}")

print("\n".join(output))