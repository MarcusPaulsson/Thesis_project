def min_blows_to_defeat_zmei(t, queries):
    results = []
    for query in queries:
        n, x, blows = query
        min_blows = float('inf')
        possible = False

        # Check each blow type
        for d, h in blows:
            # If we can defeat with this blow
            if d >= x:
                min_blows = min(min_blows, 1)
                possible = True
            else:
                # Calculate how many blows are needed to bring the heads to 0
                # After a blow we will have curX - d + h heads
                remaining_heads = x
                blows_count = 0

                while remaining_heads > 0:
                    # Deal a blow
                    blows_count += 1
                    remaining_heads -= d
                    if remaining_heads <= 0:
                        break
                    # Heads grow back
                    remaining_heads += h

                if remaining_heads <= 0:
                    min_blows = min(min_blows, blows_count)
                    possible = True

        results.append(min_blows if possible else -1)

    return results

# Read input
t = int(input())
queries = []
for _ in range(t):
    n, x = map(int, input().split())
    blows = [tuple(map(int, input().split())) for _ in range(n)]
    queries.append((n, x, blows))

# Get results
results = min_blows_to_defeat_zmei(t, queries)

# Print results
for result in results:
    print(result)