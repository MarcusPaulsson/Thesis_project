def is_beautiful(array, k):
    subarray_sums = set()
    for i in range(len(array) - k + 1):
        subarray_sum = sum(array[i:i+k])
        subarray_sums.add(subarray_sum)
    return len(subarray_sums) == 1

def create_beautiful_array(n, k, a):
    elements = list(set(a))
    
    if len(elements) > k:
        return -1  # Impossible to create a beautiful array
    
    result = []
    for i in range(k):
        result.append(elements[i % len(elements)])
    
    # Create a beautiful array by repeating the pattern
    m = 10000
    beautiful_array = (result * (m // k + 1))[:m]
    
    return m, beautiful_array

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    result = create_beautiful_array(n, k, a)
    
    if result == -1:
        print(-1)
    else:
        m, beautiful_array = result
        print(m)
        print(' '.join(map(str, beautiful_array)))