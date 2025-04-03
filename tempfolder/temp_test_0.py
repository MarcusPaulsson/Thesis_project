def solve():
    import sys
    from collections import defaultdict

    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []

    for _ in range(t):
        n = int(data[index])
        index += 1
        
        words = []
        word_set = set()
        reversals = []
        for i in range(n):
            word = data[index]
            index += 1
            
            words.append(word)
            word_set.add(word)
            reversals.append((word[::-1], i + 1))  # (reversed word, original index)

        reverse_map = defaultdict(int)
        for word in words:
            reverse_map[(word[0], word[-1])] += 1
        
        total_reversals = 0
        to_reverse = []

        for rev_word, orig_index in reversals:
            if reverse_map[(rev_word[0], rev_word[-1])] > 0:
                reverse_map[(rev_word[0], rev_word[-1])] -= 1
                to_reverse.append(orig_index)
                total_reversals += 1

        if total_reversals == n:
            results.append(f"{total_reversals}")
            results.append(" ".join(map(str, to_reverse)))
        else:
            results.append("-1")

    print("\n".join(results))

if __name__ == "__main__":
    solve()