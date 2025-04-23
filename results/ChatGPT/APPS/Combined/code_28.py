def rename_files(n, files):
    examples = []
    regulars = []
    
    for name, type_ in files:
        if type_ == '1':
            examples.append(name)
        else:
            regulars.append(name)
    
    moves = []
    # Move examples to their new names
    for i, example in enumerate(examples):
        new_name = str(i + 1)
        moves.append(f"move {example} {new_name}")
    
    # Move regular tests to their new names
    for i, regular in enumerate(regulars):
        new_name = str(len(examples) + i + 1)
        moves.append(f"move {regular} {new_name}")
    
    print(len(moves))
    for move in moves:
        print(move)

# Read input
n = int(input())
files = [input().split() for _ in range(n)]

rename_files(n, files)