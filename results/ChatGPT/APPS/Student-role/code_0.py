def solve():
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
        
        pairs = {}
        reversed_pairs = {}
        
        for i, word in enumerate(words):
            first, last = word[0], word[-1]
            if (first, last) in pairs:
                pairs[(first, last)].append(i + 1)
            else:
                pairs[(first, last)] = [i + 1]
                
            rev_first, rev_last = last, first
            if (rev_first, rev_last) in reversed_pairs:
                reversed_pairs[(rev_first, rev_last)].append(i + 1)
            else:
                reversed_pairs[(rev_first, rev_last)] = [i + 1]
        
        # Check for possible connections
        used = set()
        reversed_used = set()
        reversals = []
        
        for (first, last), indices in pairs.items():
            if (last, first) in reversed_pairs and (last, first) not in used:
                # If we have both a normal and a reversed word pair
                used.add((first, last))
                used.add((last, first))
                # We can connect them
                continue
            if (first, last) not in used:
                # No reversed pair, mark this as needing reversal
                reversals.append(indices[0])  # Take one of them to reverse
                reversed_used.add((last, first))
        
        # Check if all pairs are used
        if len(used) + len(reversed_used) != len(pairs):
            results.append("-1")
        else:
            results.append(f"{len(reversals)}")
            if reversals:
                results.append(' '.join(map(str, reversals)))
    
    sys.stdout.write("\n".join(results) + "\n")

solve()