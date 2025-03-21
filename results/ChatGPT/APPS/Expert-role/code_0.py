def process_test_case(n, words):
    pairs = {}
    to_reverse = set()
    
    for i in range(n):
        word = words[i]
        rev_word = word[::-1]
        
        if (word[0], word[-1]) in pairs:
            return -1  # Conflict, can't arrange
        pairs[(word[0], word[-1])] = i + 1  # Store index (1-based)
        
        if (rev_word[0], rev_word[-1]) in pairs:
            to_reverse.add(pairs[(rev_word[0], rev_word[-1])])  # Mark for reversal
        else:
            pairs[(rev_word[0], rev_word[-1])] = -(i + 1)  # Store index of the reversed word (negative)

    result = []
    for idx in to_reverse:
        result.append(abs(idx))
    
    return len(result), result

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        words = data[index + 1:index + 1 + n]
        index += n + 1
        
        k, reversed_indices = process_test_case(n, words)
        if k == -1:
            results.append("-1")
        else:
            results.append(f"{k}")
            if k > 0:
                results.append(" ".join(map(str, reversed_indices)))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()