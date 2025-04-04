def minimal_lexicographic_string(s):
    from collections import Counter
    
    char_count = Counter(s)
    result = []

    while char_count:
        smallest_char = min(char_count)
        result.append(smallest_char)
        char_count[smallest_char] -= 1
        
        if char_count[smallest_char] == 0:
            del char_count[smallest_char]
    
    return ''.join(result)

s = input().strip()
result = minimal_lexicographic_string(s)
print(result)