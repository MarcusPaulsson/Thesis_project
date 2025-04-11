def rename_files(n, files):
    examples = []
    regulars = []
    
    # Separate files into examples and regular tests
    for name, type_ in files:
        if type_ == '1':
            examples.append(name)
        else:
            regulars.append(name)
    
    # Prepare the moves
    moves = []
    
    # Rename examples
    for i, example in enumerate(examples):
        moves.append(f"move {example} {i + 1}")
    
    # Rename regular tests
    for i, regular in enumerate(regulars):
        moves.append(f"move {regular} {len(examples) + i + 1}")
    
    # Output the result
    print(len(moves))
    print("\n".join(moves))

# Read input
n = int(input())
files = [input().split() for _ in range(n)]
rename_files(n, files)