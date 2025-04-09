def rename_files(n, files):
    examples = []
    regulars = []
    
    # Separate examples and regular tests
    for file in files:
        name, type_ = file.split()
        if type_ == '1':
            examples.append(name)
        else:
            regulars.append(name)
    
    # Prepare the moves
    moves = []
    
    # Move examples to 1, 2, ..., e
    for i, example in enumerate(examples):
        target_name = str(i + 1)
        moves.append(f"move {example} {target_name}")
    
    # Move regulars to e + 1, e + 2, ..., n
    for i, regular in enumerate(regulars):
        target_name = str(len(examples) + i + 1)
        moves.append(f"move {regular} {target_name}")
    
    # Output the results
    print(len(moves))
    print("\n".join(moves))

# Input processing
n = int(input().strip())
files = [input().strip() for _ in range(n)]

# Call the function with the input
rename_files(n, files)