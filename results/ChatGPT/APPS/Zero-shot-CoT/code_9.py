def alice_score(s):
    score_alice = 0
    score_bob = 0
    current_char = None
    count = 0
    
    # Count the number of 1's and group them by segments
    for char in s:
        if char == current_char:
            count += 1
        else:
            if current_char == '1':
                score_alice += count if (count % 2 == 1) else count // 2
                score_bob += count // 2
            count = 1
            current_char = char
            
    # Last segment
    if current_char == '1':
        score_alice += count if (count % 2 == 1) else count // 2
        score_bob += count // 2

    return score_alice

# Read input
T = int(input())
for _ in range(T):
    s = input().strip()
    print(alice_score(s))