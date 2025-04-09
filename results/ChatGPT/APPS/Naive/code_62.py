def min_operations(test_cases):
    results = []
    
    for a, b, c in test_cases:
        min_moves = float('inf')
        best_triplet = (a, b, c)
        
        for A in range(1, a + 1):
            for B in range(A, 10001):
                if B % A != 0:
                    continue
                for C in range(B, 10001):
                    if C % B == 0:
                        moves = abs(A - a) + abs(B - b) + abs(C - c)
                        if moves < min_moves:
                            min_moves = moves
                            best_triplet = (A, B, C)

        results.append((min_moves, best_triplet))
    
    return results

def main():
    t = int(input())
    test_cases = [tuple(map(int, input().split())) for _ in range(t)]
    results = min_operations(test_cases)
    
    for moves, triplet in results:
        print(moves)
        print(*triplet)

if __name__ == "__main__":
    main()