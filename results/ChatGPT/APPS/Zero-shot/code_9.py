def alice_score(s):
    # Count the number of '1's in each segment of consecutive '1's
    segments = []
    count = 0
    for char in s:
        if char == '1':
            count += 1
        else:
            if count > 0:
                segments.append(count)
            count = 0
    if count > 0:
        segments.append(count)
    
    # Alice's score is the sum of the '1's at even indices (0-based)
    alice_score = sum(segments[i] for i in range(0, len(segments), 2))
    return alice_score

T = int(input())
for _ in range(T):
    s = input().strip()
    print(alice_score(s))