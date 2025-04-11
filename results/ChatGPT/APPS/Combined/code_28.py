def rename_files(n, files):
    examples = []
    regulars = []
    
    # Separate files into examples and regular tests
    for name, type_ in files:
        if type_ == '1':
            examples.append(name)
        else:
            regulars.append(name)
    
    # Prepare the output script
    moves = []
    
    # Rename example files to 1, 2, ..., e
    for i, example in enumerate(examples):
        new_name = str(i + 1)
        moves.append(f"move {example} {new_name}")
    
    # Rename regular files to e + 1, e + 2, ..., n
    for i, regular in enumerate(regulars):
        new_name = str(len(examples) + i + 1)
        moves.append(f"move {regular} {new_name}")
    
    # Output the results
    print(len(moves))
    for move in moves:
        print(move)

# Read input
n = int(input())
files = [input().split() for _ in range(n)]

# Call the function
rename_files(n, files)