def clean_binary_string(s):
    # Count the number of 0s and 1s
    count_0 = s.count('0')
    count_1 = s.count('1')
    
    # The cleanest string will be all 0s followed by all 1s
    return '0' * count_0 + '1' * count_1

t = int(input())
results = []
for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    results.append(clean_binary_string(s))

print('\n'.join(results))