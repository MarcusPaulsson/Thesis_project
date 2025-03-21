def k_amazing_numbers(test_cases):
    results = []
    for a in test_cases:
        n = len(a)
        last_position = {}
        min_occur = [float('inf')] * (n + 1)
        
        for i in range(n):
            last_position[a[i]] = i
            
        for i in range(n):
            if a[i] in last_position:
                # Calculate the distance to the next position of the same number
                if a[i] in min_occur:
                    min_occur[a[i]] = min(min_occur[a[i]], i - last_position[a[i]])
                else:
                    min_occur[a[i]] = i - last_position[a[i]]
                last_position[a[i]] = i
        
        # Handle for the last occurrences
        for key, value in last_position.items():
            if key in min_occur:
                min_occur[key] = min(min_occur[key], n - value)

        k_amazing = [-1] * n
        for number, distance in min_occur.items():
            if distance < n:
                k_amazing[distance] = min(k_amazing[distance], number) if k_amazing[distance] != -1 else number

        for i in range(n - 1, 0, -1):
            k_amazing[i] = min(k_amazing[i], k_amazing[i + 1]) if k_amazing[i + 1] != -1 else k_amazing[i]
        
        results.append(k_amazing[1:n + 1])
    
    return results

# Reading input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
index = 1
test_cases = []

for _ in range(t):
    n = int(data[index])
    a = list(map(int, data[index + 1].split()))
    test_cases.append(a)
    index += 2

results = k_amazing_numbers(test_cases)

# Printing output
for result in results:
    print(" ".join(map(str, result)))