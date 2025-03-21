def process_test_case(n, words):
    word_set = set(words)
    reversals = []
    
    for i in range(n):
        if words[i][::-1] in word_set:
            reversals.append(i + 1)  # Store 1-based index of the word

    if len(reversals) % 2 == 1:
        # If odd number of reversals, we can't pair them correctly
        return -1
    
    return len(reversals), reversals


def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        words = [data[index + i] for i in range(n)]
        index += n
        
        result = process_test_case(n, words)
        if result == -1:
            results.append("-1")
        else:
            k, reversals = result
            results.append(f"{k}")
            if k > 0:
                results.append(" ".join(map(str, reversals)))
    
    print("\n".join(results))


if __name__ == "__main__":
    main()