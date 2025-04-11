def rename_files(n, files):
    examples = []
    regulars = []
    
    for name, type_ in files:
        if type_ == '1':
            examples.append(name)
        else:
            regulars.append(name)
    
    moves = []
    # Rename examples to 1, 2, ..., e
    for i in range(len(examples)):
        moves.append(f"move {examples[i]} {i + 1}")
    
    # Rename regular tests to e + 1, e + 2, ..., n
    for i in range(len(regulars)):
        moves.append(f"move {regulars[i]} {len(examples) + i + 1}")
    
    return len(moves), moves

# Input reading
n = int(input())
files = [input().split() for _ in range(n)]

# Get the result
num_moves, move_commands = rename_files(n, files)

# Output the result
print(num_moves)
for command in move_commands:
    print(command)