def rename_files(n, files):
    examples = []
    regulars = []
    
    # Separate examples and regular tests
    for name, typ in files:
        if typ == '1':
            examples.append(name)
        else:
            regulars.append(name)

    moves = []
    # Move examples to their new names
    for i in range(len(examples)):
        moves.append(f"move {examples[i]} {i + 1}")
    
    # Move regular tests to their new names
    for i in range(len(regulars)):
        moves.append(f"move {regulars[i]} {len(examples) + i + 1}")

    # Output the result
    print(len(moves))
    for move in moves:
        print(move)

# Read input
n = int(input().strip())
files = [input().strip().split() for _ in range(n)]

rename_files(n, files)