t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # We can simply sort the arrays and pair them
    a.sort()
    b.sort()
    
    # Output the sorted arrays
    print(" ".join(map(str, a)))
    print(" ".join(map(str, b)))