def create_rename_script(n, files):
    examples = []
    regulars = []
    
    for name, file_type in files:
        if file_type == '1':
            examples.append(name)
        else:
            regulars.append(name)
    
    total_files = n
    e = len(examples)
    
    moves = []
    
    # Renaming examples to 1, 2, ..., e
    for i in range(e):
        moves.append(f"move {examples[i]} {i + 1}")
    
    # Renaming regular tests to e + 1, e + 2, ..., n
    for i in range(len(regulars)):
        moves.append(f"move {regulars[i]} {e + i + 1}")
    
    # Final output
    print(len(moves))
    print("\n".join(moves))

if __name__ == "__main__":
    n = int(input().strip())
    files = [input().strip().split() for _ in range(n)]
    create_rename_script(n, files)