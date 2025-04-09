def rename_files(n, files):
    examples = []
    regulars = []

    # Split files into examples and regular tests
    for name, type_ in files:
        if type_ == '1':
            examples.append(name)
        else:
            regulars.append(name)

    # Prepare the result
    moves = []
    
    # Rename examples to 1, 2, ..., e
    for i, example_name in enumerate(examples):
        new_name = str(i + 1)
        moves.append(f"move {example_name} {new_name}")

    # Rename regular tests to e + 1, e + 2, ..., n
    e = len(examples)
    for i, regular_name in enumerate(regulars):
        new_name = str(e + i + 1)
        current_name = regular_name if i == 0 else str(e + i)
        moves.append(f"move {current_name} {new_name}")

    # Output results
    print(len(moves))
    print("\n".join(moves))

# Read input
n = int(input().strip())
files = [input().strip().split() for _ in range(n)]

rename_files(n, files)