def rename_files(n, files):
    examples = []
    regulars = []
    
    # Separate examples and regular tests
    for name, type_ in files:
        if type_ == '1':
            examples.append(name)
        else:
            regulars.append(name)
    
    # Prepare the moves
    moves = []
    # Move examples to 1, 2, ..., e
    for i, example in enumerate(examples):
        moves.append(f"move {example} {i + 1}")
    
    # Move regular tests to e + 1, e + 2, ..., n
    for i, regular in enumerate(regulars):
        moves.append(f"move {regular} {len(examples) + i + 1}")
    
    # Output the result
    print(len(moves))
    for move in moves:
        print(move)

# Input reading
n = int(input().strip())
files = [input().strip().split() for _ in range(n)]

# Call the function
rename_files(n, files)