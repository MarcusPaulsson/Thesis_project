def max_chess_score(t, test_cases):
    results = []
    for n, k, s in test_cases:
        # Calculate initial score
        score = 0
        for i in range(n):
            if s[i] == 'W':
                if i == 0 or s[i - 1] == 'L':
                    score += 1
                else:
                    score += 2
        
        # Now we have the initial score, let's try to maximize it
        # Count the number of wins and losses
        win_segments = []
        current_wins = 0
        
        for i in range(n):
            if s[i] == 'W':
                current_wins += 1
            else:
                if current_wins > 0:
                    win_segments.append(current_wins)
                current_wins = 0
        
        if current_wins > 0:
            win_segments.append(current_wins)
        
        # Calculate potential gains from changing losses to wins
        max_score = score
        max_gains = []
        
        for segment in win_segments:
            if segment > 0:
                max_gains.append(segment * 2 - 1)  # Each segment can be extended by 1 win
            else:
                max_gains.append(1)  # Each loss can be converted to a win, gaining 1 point
        
        # Sort from maximum gain to minimum gain
        max_gains.sort(reverse=True)

        # Apply changes based on the allowed k
        for i in range(min(k, len(max_gains))):
            max_score += max_gains[i]
        
        results.append(max_score)
    
    return results

# Example usage:
t = 8
test_cases = [
    (5, 2, "WLWLL"),
    (6, 5, "LLLWWL"),
    (7, 1, "LWLWLWL"),
    (15, 5, "WWWLLLWWWLLLWWW"),
    (40, 7, "LLWLWLWWWLWLLWLWWWLWLLWLLWLLLLWLLWWWLWWL"),
    (1, 0, "L"),
    (1, 1, "L"),
    (6, 1, "WLLWLW")
]

print(max_chess_score(t, test_cases))