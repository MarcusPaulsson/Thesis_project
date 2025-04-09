def solve():
    n = int(input())
    files = []
    for _ in range(n):
        files.append(input().split())
    
    examples = []
    regular = []
    
    for i in range(n):
        if files[i][1] == '1':
            examples.append((files[i][0], i))
        else:
            regular.append((files[i][0], i))
            
    e = len(examples)
    
    moves = []
    
    # Move examples to 1, 2, ..., e
    for i in range(e):
        if examples[i][0] != str(i + 1):
            
            # Find a temporary name
            temp_name = "temp" + str(i)
            while any(f[0] == temp_name for f in files):
                temp_name = "temp" + str(i) + str(i)
            
            # Move example to temp
            moves.append(f"move {examples[i][0]} {temp_name}")
            
            # Move correct number to example's spot
            
            found = False
            for j in range(n):
                if files[j][0] == str(i + 1):
                    moves.append(f"move {str(i + 1)} {examples[i][0]}")
                    found = True
                    break
            if not found:

                moves.append(f"move {i+1} {examples[i][0]}")


            # Move temp to correct number
            moves.append(f"move {temp_name} {i+1}")

    
    # Move regular tests to e+1, e+2, ..., n
    for i in range(len(regular)):
        if regular[i][0] != str(e + i + 1):
            
            temp_name = "temp" + str(e + i + 1)
            while any(f[0] == temp_name for f in files):
                temp_name = "temp" + str(e + i + 1) + str(i)
            
            moves.append(f"move {regular[i][0]} {temp_name}")
            
            found = False
            for j in range(n):
                if files[j][0] == str(e + i + 1):
                    moves.append(f"move {str(e + i + 1)} {regular[i][0]}")
                    found = True
                    break
            if not found:
                moves.append(f"move {e+i+1} {regular[i][0]}")
            
            moves.append(f"move {temp_name} {e+i+1}")
            
    print(len(moves))
    for move in moves:
        print(move)

solve()