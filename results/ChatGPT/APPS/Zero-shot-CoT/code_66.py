t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # Sort both lists to ensure distinct sums when paired
    a.sort()
    b.sort()
    
    # Output the results
    print(' '.join(map(str, a)))
    print(' '.join(map(str, b)))