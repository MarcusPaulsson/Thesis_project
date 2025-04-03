t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    found = False
    # We will use a dictionary to keep track of the last seen index of each number
    last_seen = {}
    
    for i in range(n):
        if a[i] in last_seen:
            # If we see the same number again, we can form a palindrome of length at least 3
            if i - last_seen[a[i]] >= 2:
                found = True
                break
        last_seen[a[i]] = i
    
    print("YES" if found else "NO")