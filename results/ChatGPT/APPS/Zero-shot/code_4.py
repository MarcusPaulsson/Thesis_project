n = int(input())
a = list(map(int, input().split()))

# Get the minimum and maximum values in the array
min_a = min(a)
max_a = max(a)

# If all values are already equal, D can be 0
if min_a == max_a:
    print(0)
else:
    # Calculate the required D
    D = (max_a - min_a) // 2
    
    # Check if D can make all elements equal
    if (max_a - min_a) % 2 == 0:
        # Check if we can choose D such that all values can be made equal
        target1 = min_a + D
        target2 = max_a - D
        
        if target1 == target2:
            print(D)
        else:
            print(-1)
    else:
        print(-1)