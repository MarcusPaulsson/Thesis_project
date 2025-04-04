def max_beauty_after_swap(n, trophies):
    segments = []
    current_length = 0
    
    for trophy in trophies:
        if trophy == 'G':
            current_length += 1
        else:
            if current_length > 0:
                segments.append(current_length)
            current_length = 0
            
    if current_length > 0:
        segments.append(current_length)
    
    if not segments:  # No golden trophies
        return 0
    
    max_length = max(segments)
    
    for i in range(len(segments) - 1):
        combined_length = segments[i] + segments[i + 1]
        max_length = max(max_length, combined_length)
    
    if 'S' in trophies:  # Check for silver trophies
        max_length += 1
    
    return max_length

if __name__ == "__main__":
    n = int(input().strip())
    trophies = input().strip()
    print(max_beauty_after_swap(n, trophies))